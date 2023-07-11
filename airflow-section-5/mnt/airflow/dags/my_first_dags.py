# to create the DAG object
from airflow import DAG

#Opreators
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

#datetime
from datetime import timedelta,datetime

#initialize your default arguments

default_args={
'owner':'ankur',
'start_date':datetime(2022,3,4),
'retries':3,
'retry_delay':timedelta(minutes=5)
}

#instantiate a DAG object
myfirst_dag=DAG('my_first_dag',default_args=default_args,
catchup=False,
tags=['example, myfirstdags']
)

#python function

def my_first_func():
    return 'HEY ,this is my first dag'
    
# create first task
start_task=DummyOperator(task_id='start_task',dag=myfirst_dag)

# create second task

first_dag_task=PythonOperator(task_id='first_dag_task',
python_callable=my_first_func,dag=myfirst_dag)

#create third task
end_task=DummyOperator(task_id='end_task',dag=myfirst_dag)

#set the dependancy
start_task>> first_dag_task>> end_task
