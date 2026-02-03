from airflow.sdk import dag, task, task_group
from datetime import datetime

@dag(
    dag_id="group_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def group():

    @task
    def a():
        return 42

    @task_group(default_args={
        'retries': 2 # Retry 2 times in this Group
    })
    def my_group(val: int):

        @task
        def b(my_val: int):
            print(my_val + 42)

        @task_group(default_args={
            'retries': 3 # Retry 3 times in this Group
        })
        def my_nested_group():   

            @task
            def c():
                print('c')
            
            c()

        b(val) >> my_nested_group()    

    val = a() 
    my_group(val) # Share value from task A to B

group()