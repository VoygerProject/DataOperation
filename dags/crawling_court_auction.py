from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'python_script_dag',
    default_args=default_args,
    description='법원경매 크롤링 DAG',
    schedule_interval='0 13 * * *',
)

run_python_script = BashOperator(
    task_id='run_python_script',
    bash_command='python /opt/projects/crawler/src/crawler.py',
    dag=dag,
)

run_python_script
