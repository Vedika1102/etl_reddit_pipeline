import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Ensure the correct path to 'pipelines' is included
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sys.path.append(os.path.abspath('/opt/airflow'))
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'Vedika Shinde',
    'start_date': datetime(2025, 2, 16)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Extraction task
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_limit': 'day',
        'limit': 100
    },
    dag=dag
)
