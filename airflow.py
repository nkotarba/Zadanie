from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "natalia",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="medallion_pipeline_single_entry",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_pipeline = BashOperator(
        task_id="run_full_pipeline",
        bash_command="spark-submit pipeline.py"
    )

