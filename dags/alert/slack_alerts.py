from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

SLACK_CONN_ID = 'slack_conn_id'

def task_send_success_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    slack_msg = """
            :large_green_circle: Task Success.\n
            *Task*: `{task}`\n
            *dag*: `{dag}`\n
            *Execution Time*: `{exec_date}`\n
            *Log Url*: `{log_url}`\n
            """.format(
            task=context.get('task_instance').task_id,
            dag=context.get('task_instance').dag_id,
            ti=context.get('task_instance'),
            exec_date=context.get('execution_date'),
            log_url=context.get('task_instance').log_url,
        )
    print(slack_msg)
    success_alert = SlackWebhookOperator(
        task_id='slack_test',
        http_conn_id=SLACK_CONN_ID,
        webhook_token=slack_webhook_token,
        message=slack_msg,
        username='airflow')
    return success_alert.execute(context=context)
