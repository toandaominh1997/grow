import os
from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = 'mlops_model'

with DAG(
    DAG_ID,
    description='A MLOps tutorial in Airflow',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['training', 'docker'],

) as dag:
    preprocess = DockerOperator(
        task_id='preprocess',
        image='toandaominh1997/test:latest',
        command='python main.py preprocess=true',
        api_version = 'auto',
        auto_remove = True,
        docker_url='unix://var/run/docker.sock',  # Set your docker URL
        network_mode='host',
        mount_tmp_dir=False
    )
    train = DockerOperator(
        task_id='train',
        image='toandaominh1997/test:latest',
        command='python main.py train=true',
        api_version = 'auto',
        auto_remove = True,
        docker_url='unix://var/run/docker.sock',  # Set your docker URL
        network_mode='host',
        mount_tmp_dir=False
    )
    preprocess >> train
