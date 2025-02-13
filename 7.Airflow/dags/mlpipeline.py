from airflow import DAG 
# used to define task based on python function 
from airflow.operators.python import PythonOperator 
from datetime import datetime

## Define our task 
def preprocess_data():
    print('Preprocessing data...')

## define our task 2
def train_model():
    print('Traning model...')

## define our task 3
def evaluate_model():
    print('Evaluate models...')


# define the DAG
with DAG(
    'ml_pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval='@weekly',     # we can use daily, weekly, 
) as dag:
    # define the task
    preprocess=PythonOperator(task_id='preprocess_task',python_callable=preprocess_data)
    train=PythonOperator(task_id='train_task',python_callable=train_model)
    eval=PythonOperator(task_id='evaluate_model',python_callable=evaluate_model)


    # set dependencies 
    preprocess >> train >> eval 

    