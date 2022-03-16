import airflow
from alert import slack_alerts
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator

from datetime import datetime
from datetime import timedelta

from alert.slack_alerts import task_send_success_slack_alert

def _choose_best_model():
    accuracy = 6
    if accuracy > 5:
        return 'accurate'
    else:
        return 'inaccurate'

with DAG(
    dag_id='choose_best_model',
    schedule_interval="@daily",
    default_args={
        'owner': 'Fakri',
        'depends_on_past': False,
        'start_date': datetime(2022, 1, 12),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=2),
        'on_success_callback': slack_alerts.task_send_success_slack_alert
    },
    ) as dag:
        start = DummyOperator(
                task_id ='start')

        branch_task = BranchPythonOperator(
                task_id='choose_best_model',
                python_callable=_choose_best_model)   

        dummy_task_1 = DummyOperator(
                task_id='accurate',
                retries=3)

        dummy_task_2 = DummyOperator(
                task_id= 'inaccurate',
                retries=3)

start >> branch_task >> [dummy_task_1, dummy_task_2]