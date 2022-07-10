import os
from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = 'docker_test'

with DAG(
    DAG_ID,
    description='A docker tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['training', 'docker'],

) as dag:
    t1 = BashOperator(task_id='print_date', bash_command='date', dag=dag)
    t2 = BashOperator(task_id='sleep', bash_command='sleep 5', retries=3, dag=dag)
    t3 = DockerOperator(
        task_id='docker_op_main',
        image='toandaominh1997/test:latest',
        command='python main.py',
        api_version = 'auto',
        auto_remove = True,
        docker_url='unix://var/run/docker.sock',  # Set your docker URL
        network_mode='bridge',
        mount_tmp_dir=False
    )
    t4 = BashOperator(task_id='print_hello', bash_command='echo "hello world!!!"', dag=dag)
    t1 >> t2
    t1 >> t3
    t3 >> t4
