from airflow.sdk import dag, task
from datetime import datetime
import pandas as pd
from airflow.hooks.base import BaseHook # To get the Airflow's connection
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.models import Variable

@dag(
    dag_id="crypto_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def crypto():

    @task
    def upload_to_s3():
        import requests, json

        # Using Airflow variables option
        api_key = Variable.get("coincap_api_key")

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.get("https://rest.coincap.io/v3/assets",
                                headers=headers,
                                timeout=30)
        
        response.raise_for_status()

        data = response.json()["data"]

        s3 = S3Hook(aws_conn_id="aws_s3")

        key = f"crypto/{datetime.now().strftime('%Y-%m-%d')}/assets.json"

        s3.load_string(
            string_data=json.dumps(data),
            key=key,
            bucket_name="crypto-airflow-project",
            replace=True,
        )

    upload_to_s3()

crypto()