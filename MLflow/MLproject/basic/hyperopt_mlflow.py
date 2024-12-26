from mlflow_utils import create_dataset,create_mlflow_experiment
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

from hyperopt import hp,fmin,tpe,Trials

from typing import Dict,List, Optional

import pandas as pd
import mlflow
from functools import partial


def get_classification_metrics(y_true:pd.Series,y_pred:pd.Series,prefix:str)->Dict[str,float]:
    """
    calculate classification metrics
    """
    accuracy=accuracy_score(y_true,y_pred)
    precision=precision_score(y_true,y_pred)
    recall=recall_score(y_true,y_pred)
    f1=f1_score(y_true,y_pred)
    return {
        f'{prefix}_accuracy':accuracy,
        f'{prefix}_precision':precision,
        f'{prefix}_recall':recall,
        f'{prefix}_f1':f1
    }

def get_sklearn_pipeline(
        numerical_features:List[str],categorical_features:Optional[List[str]]=[]) -> Pipeline:
    """
    Get sklearn pipeline

    :param numerical_features: list of numerical features
    :param category_features: list of category features
    :return: sklearn pipeline
    """
    preprocessing=ColumnTransformer(
        transformers=[
            ('numerical',SimpleImputer(strategy='median'),numerical_features),
            ('categorical',OneHotEncoder(),categorical_features),
        ]
    )
    pipeline=Pipeline(
        steps=[
            ('preprocessing',preprocessing),
            ('model',RandomForestClassifier())
        ]
    )
    return pipeline

def objective_function(
       params:Dict,
       xtrain:pd.DataFrame,
       xtest:pd.DataFrame,
       ytrain:pd.DataFrame,
       ytest:pd.DataFrame,
       numerical_features:List[str],
       category_features:List[str], 
)->float:
    """
    objective function for hyperopt
    params params: hyperparameters values 
    params xtrain: training features
    params xtest: testing features
    params ytrain: training target
    params ytest: testing target
    params numerical_features: numerical features
    params category_features: category features
    """
    pipeline=get_sklearn_pipeline(numerical_features,category_features)
    params.update({'model__max_depth':int(params['model__max_depth'])})
    params.update({'model__n_estimators':int(params['model__n_estimators'])})
    pipeline.set_params(**params)

    with mlflow.start_run(nested=True) as run:
        pipeline.fit(xtrain,ytrain)
        ypred=pipeline.predict(xtest)
        metrics=get_classification_metrics(y_true=ytest,y_pred=ypred,prefix='test')
        
        mlflow.log_params(pipeline['model'].get_params())
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(pipeline,f'{run.info.run_id}-model')
    return -metrics['test_f1']


if __name__=='__main__':
    df=create_dataset()
    xtrain,xtest,ytrain,ytest=train_test_split(df.drop('target',axis=1),df['target'],test_size=0.2,random_state=42)
    numerical_features=[f for f in xtrain.columns if f.startswith('feature')]
    print(numerical_features)

    space={
        'model__n_estimators':hp.quniform('model__n_estimators',20,200,10),
        'model__max_depth':hp.quniform('model__max_depth',10,100,10),
    }

    experiment_id=create_mlflow_experiment(experiment_name='hyperopt_experiment',artifact_location='hyperopt_mlflow_artifact',tags={'type':'hyperopt'})

    with mlflow.start_run(run_name='hyperparameter_optimization') as run:
        best_params=fmin(
            fn=partial(
                objective_function,
                xtrain=xtrain,
                xtest=xtest,
                ytrain=ytrain,
                ytest=ytest,
                numerical_features=numerical_features,
                category_features=[]
            ),
            space=space,
            algo=tpe.suggest,
            max_evals=10,
            trials=Trials()
        )
        pipeline=get_sklearn_pipeline(numerical_features=numerical_features)

        best_params.update({'model__max_depth':int(best_params['model__max_depth'])})
        best_params.update({'model__n_estimators':int(best_params['model__n_estimators'])})
        pipeline.set_params(**best_params)
        pipeline.fit(xtrain,ytrain)
        ypred=pipeline.predict(xtest)
        metrics=get_classification_metrics(y_true=ytest,y_pred=ypred,prefix='best_model_test')
        mlflow.log_params(pipeline['model'].get_params())
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(pipeline,f'{run.info.run_id}-best_model',registered_model_name='hyperopt_best_model')
