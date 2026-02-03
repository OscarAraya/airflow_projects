from airflow.sdk import dag, task
from time import sleep
from datetime import datetime

@dag(
    dag_id="celery_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def celery_dag():

    @task
    def a():
        sleep(5)
    
    @task(
            queue='queue_name' # Used to set the task to a specific queue
    )
    def b():
        sleep(5)

    @task
    def c():
        sleep(5)

    @task
    def d():
        sleep(5)

    a() >> [b(), c()] >> d()

celery_dag()