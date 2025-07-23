from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'stratum',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='stratum_example_dag',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=["stratum"]
) as dag:

    task1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from Stratum!"'
    )
