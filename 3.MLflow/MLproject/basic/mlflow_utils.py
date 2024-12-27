import mlflow
from typing import Any
import mlflow.entities
import pandas as pd 
from sklearn.datasets import make_classification


def create_mlflow_experiment(experiment_name:str,artifact_location:str,tags:dict[str:Any])->str:
    """ 
    create a new experiment with the given name and artifact location 
    """
    try: 
        experiment_id=mlflow.create_experiment(name=experiment_name,artifact_location=artifact_location,tags=tags)
    except:
        print(f'Experiment {experiment_name} already exists')
        experiment_id=mlflow.get_experiment_by_name(experiment_name).experiment_id

    mlflow.set_experiment(experiment_name=experiment_name)


def get_mlflow_experiment(experiment_id:str=None,experiment_name:str=None)-> mlflow.entities.Experiment:
    """
    returns an experiment entity
    """
    if experiment_id is not None:
        experiment=mlflow.get_experiment(experiment_id=experiment_id)
    elif experiment_name is not None:
        experiment=mlflow.get_experiment_by_name(experiment_name)
    else:
        raise ValueError('Either experiment_id or experiment_name must be provided')
    return experiment


def delete_mlflow_experiment(experiment_id:str=None,experiment_name:str=None)->None:
    """ 
    delete an experiment 
    """
    if experiment_id is not None:
        mlflow.delete_experiment(experiment_id=experiment_id)
    elif experiment_name is not None:
        experiment=get_mlflow_experiment(experiment_name=experiment_name)
        experiment_id=experiment.experiment_id
        mlflow.delete_experiment(experiment_id=experiment_id)
    else:
        raise ValueError('Either experiment_id or experiment_name must be provided')


def create_dataset(n_samples:int=10000,n_features:int=50,n_informative:int=10,class_sep:float=0.3,random_state:int=None)-> pd.DataFrame:
    """ 
    create a dataset for testing purpose
    """
    x,y=make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_informative,
        class_sep=class_sep,
        random_state=random_state
    )

    df=pd.DataFrame(x,columns=[f'feature_{i}' for i in range(n_features)])
    df['target']=y

    return df
