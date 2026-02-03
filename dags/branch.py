from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="branch_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def branch():

    @task
    def a():
        return 1

    @task.branch 
    def b(val: int):
        if val == 1:
            return ['equal_1', 'run_if_1']
        return 'different_than_1'

    @task
    def run_if_1(val: int):
        print(f'Run if {val}')
    
    @task
    def equal_1(val: int):
        print(f'Equals to {val}')

    @task
    def different_than_1(val: int):
        print(f'Different than {val}')

    val = a()
    b(val) >> [equal_1(val) , different_than_1(val), run_if_1(val)]

branch()