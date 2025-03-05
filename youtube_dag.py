from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from youtube_api import run_youtube_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['fari_0901@yahoo.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

#create dag
dag = DAG(
    'youtube_dag',
    default_args = default_args,
    description = 'My Youtube ETL code'
)

run_etl = PythonOperator(
    task_id = 'complete_youtube_etl',
    python_callable = run_youtube_etl,
    dag = dag,
)

run_etl
