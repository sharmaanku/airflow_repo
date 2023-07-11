from airflow import DAG
from datetime import timedelta,datetime
from airflow.operators.dummy_operator
import DummyOperator


# create defaultarguments for DAG
default_args={
	'owner'='ankur'
	'start_date': datetime(2023,07,11)
}


# DAG object

dag =DAG(dag_id='My-DAG',default_args=default_args,schedule_interval='@once')


# create tasks 

start = DummyOperator(task_id='start',dag=dag)