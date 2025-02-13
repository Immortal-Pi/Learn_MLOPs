""" 
define DAG's where the tasks are as follows:

Tasks:
1. start an initial number 
2. add 5 to the number
3. multiply the result by 2
4. subtract 3 from the result 
5. compute the square of the result 

"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime 


## define function for each task 
## context - dependancy 
def start_number(**context):
    context['ti'].xcom_push(key='current_value',value=10)
    print('Starting number is 10')


def add_by_five(**context):
    current_value=context['ti'].xcom_pull(key='current_value',task_ids='start_task')
    new_value=current_value+5
    context['ti'].xcom_push(key='current_value',value=new_value)
    print(f'adding 5 to the {current_value}')


def multiply_by_two(**context):
    current_value=context['ti'].xcom_pull(key='current_value',task_ids='add_five')
    new_value=current_value*2
    context['ti'].xcom_push(key='current_value',value=new_value)
    print(f'multiplied {current_value} by 2')

def subtract_by_three(**context):
    current_value=context['ti'].xcom_pull(key='current_value',task_ids='multiply_two')
    new_value=current_value-3
    context['ti'].xcom_push(key='current_value',value=new_value)
    print(f'subtracted {current_value} by 3')

def square_the_result(**context):
    current_value=context['ti'].xcom_pull(key='current_value',task_ids='substract_three')
    new_value=current_value**2
    context['ti'].xcom_push(key='current_value',value=new_value)
    print(f'squaring {current_value}')


## define the DAG
with DAG(
   dag_id='math_sequence_dag',
   start_date=datetime(2025,1,1),
   schedule_interval='@once',
   catchup=False 
) as dag:
    ## define the task 
    ## map the task id 
    start_task=PythonOperator(
        task_id='start_task',
        python_callable=start_number,
        provide_context=True
    )
    add_five=PythonOperator(
        task_id='add_five',
        python_callable=add_by_five,
        provide_context=True
    )
    multiply_two=PythonOperator(
        task_id='multiply_two',
        python_callable=multiply_by_two,
        provide_context=True
    )
    substract_three=PythonOperator(
        task_id='substract_three',
        python_callable=subtract_by_three,
        provide_context=True
    )
    square=PythonOperator(
        task_id='square',
        python_callable=square_the_result,
        provide_context=True
    )


## dependencies 
start_task >> add_five >> multiply_two >> substract_three >> square