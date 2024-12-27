from package.feature.data_processing import get_feature_dataframe
from package.ml_training.retrieval import get_train_test_score_set
from sklearn.metrics import classification_report
import pandas as pd 
import mlflow

if __name__=='__main__':
    
    df=get_feature_dataframe()
    xtrain,xtest,xscore,ytrain,ytest,yscore=get_train_test_score_set(df)
    features=[f for f in xtrain.columns if f not in ['id','target','MedHouseVal']]

    model_uri='models:/resgistered_model/latest'
    mlflow_model=mlflow.sklearn.load_model(model_uri=model_uri)
    print(mlflow_model)
    prediction=mlflow_model.predict(xscore[features])
    scored_data=pd.DataFrame({'prediction':prediction,'target':yscore})
    classification_report=classification_report(yscore,prediction)
    print(classification_report)
    print(scored_data.head(10))