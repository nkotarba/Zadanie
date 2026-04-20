from airflow import DAG  
from airflow.operators.python import PythonOperator  
from datetime import datetime  
  
def process_bronze():  
    run_bronze_to_silver()  
  
with DAG(  
    'bronze_to_silver',  
    start_date=datetime(2026, 1, 1),  
    schedule_interval=None  # trigger only  
) as dag:  
  
    task = PythonOperator(  
        task_id='process_data',  
        python_callable=process_bronze  
    )