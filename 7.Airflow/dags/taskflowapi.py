""" 
math operation with task flow API 
Apache Airflow introduces the TaskFlow API which allows to create task using 
python decorators like @task. This is a cleaner and more intuitive way of 
writing task without needing to manually use operators like pythonOperator.
Let me show you how to modify the previous code to use the @task decorator


"""
from airflow import DAG 
from airflow.decorators import task
from datetime import datetime

### define the DAG
with DAG(
    dag_id='math_sequence_dag_with_taskflow',
    start_date=datetime(2025,1,1),
    schedule='@once',
    catchup=False,
) as dag:
    

    # task 1: start with the initial number 
    @task
    def start_number():
        initial_value=10
        print(f'the initial value is {initial_value}')
        return initial_value
    
    @task 
    def add_five(number):
        new_value=number+5
        print(f'adding 5 to {number}={new_value}')
        return new_value
    
    @task 
    def multiply_by_two(number):
        new_value=number*2
        print(f'multiplying {number} by 2 = {new_value}')
        return new_value
    
    @task 
    def subtract_three(number):
        new_value=number-3
        print(f'subtracting {number} by 3 ={new_value}')
        return new_value
    
    @task 
    def square_number(number):
        new_value=number**2
        print(f'squaring {number} = {new_value}')
        return new_value

    ## set the task dependancies 
    start_value=start_number()
    added_value=add_five(start_value)
    multiply_value=multiply_by_two(added_value)
    subtract_value=subtract_three(multiply_value)
    square_numbers=square_number(subtract_value)
