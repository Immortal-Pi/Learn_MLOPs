from package.feature.data_processing import get_feature_dataframe
from package.ml_training.retrieval import get_train_test_score_set
from package.ml_training.preprocessing_pipeline import get_pipeline
from package.utils.utils import set_or_create_experiment,get_classification_metrics,get_performance_plots
from package.package.ml_training.train import train_model
from package.utils.utils import register_model_with_client
import mlflow



if __name__=='__main__':
    experiment_name='house_pricing_classifier'
    run_name='testing_classifier'
    model_name='resgistered_model'
    artifact_path='model'
    df=get_feature_dataframe()
    # print(df.head())
    
    xtrain,xtest,xscore,ytrain,ytest,yscore=get_train_test_score_set(df)

    features=[f for f in xtrain.columns if f not in ['id','target','MedHouseVal']]

    pipeline=get_pipeline(numerical_features=features,categorical_features=[])

    experiment_id=set_or_create_experiment(experiment_name=experiment_name)

    run_id,model=train_model(pipeline=pipeline,run_name=run_name,artifact_path=artifact_path,model_name=model_name,x=xtrain[features],y=ytrain)

    ypred=model.predict(xtest)

    classification_metrics=get_classification_metrics(y_true=ytest,y_pred=ypred,prefix='test')
    performance_plot=get_performance_plots(y_pred=ypred,y_true=ytest,prefix='test')

    #register the model
    #mlflow.register_model(model_uri=f'runs:/{run_id}/{artifact_path}',name=model_name)
    # manual register # if model already registered it will throw error
    #register_model_with_client(model_name=model_name,run_id=run_id,artifact_path=artifact_path)

    # log performance metrics 
    with mlflow.start_run(run_id=run_id):
        
        # log metrics
        mlflow.log_metrics(classification_metrics)

        # log params
        mlflow.log_params(model[-1].get_params())

        # log tags 
        mlflow.set_tags({'type':'classifier'})

        # log description 
        mlflow.set_tag('mlflow.note.content','This is a classifer for the house pricing dataset')
        
        # log plots
        for plt_name,fig in performance_plot.items():
            mlflow.log_figure(fig,plt_name+'.png')
