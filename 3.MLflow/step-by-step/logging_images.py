import mlflow
from mlflow_utils import get_mlflow_experiment,create_dataset
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import PrecisionRecallDisplay
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt 

if __name__=='__main__':

    experiment =get_mlflow_experiment(experiment_name='logging_experiment')
    print(f'Name: {experiment.name}')


    with mlflow.start_run(run_name='logging_images',experiment_id=experiment.experiment_id) as run:
        
        x,y=make_classification(n_samples=10000,n_features=50,n_informative=10,class_sep=1.0,random_state=22)
        xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=43)

        rfc=RandomForestClassifier(n_estimators=100,random_state=42)
        rfc.fit(xtrain,ytrain)

        y_pred=rfc.predict(xtest)


        # log the precision-recall curve
        fig_pr=plt.figure()
        roc_display=PrecisionRecallDisplay.from_predictions(ytest,y_pred,ax=plt.gca())
        plt.title('Precision-Recall curve')
        plt.legend()
        mlflow.log_figure(fig_pr,'metrics/precision_recall_curve.png')

        # log the ROC curve
        fig_roc=plt.figure()
        roc_display=RocCurveDisplay.from_predictions(y_pred,ytest,ax=plt.gca())
        plt.title('ROC curve')
        plt.legend()
        mlflow.log_figure(fig_roc,'metrics/roc_curve.png')

        # log the confusion matrix
        fig_cm=plt.figure()
        cm_display=ConfusionMatrixDisplay.from_predictions(y_pred,ytest,ax=plt.gca())
        plt.title('Confusion Matrix')
        plt.legend()
        mlflow.log_figure(fig_cm,'metrics/confusion_matrix.png')


        #Print info about the run
        print(f'run_id: {run.info.run_id}')
        print(f'experiment_id: {run.info.experiment_id}')
        print(f'status: {run.info.status}')
        print(f'start time: {run.info.start_time}')
        print(f'end time: {run.info.end_time}')
        print(f'lifecycle stage: {run.info.lifecycle_stage}')

