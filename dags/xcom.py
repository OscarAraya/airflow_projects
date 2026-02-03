from airflow.sdk import dag, task, Context
from datetime import datetime
from typing import Dict, Any

@dag(
    dag_id="xcom_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def xcom_dag():

    @task
    def t1() -> Dict[str, Any]: # context: Context
        my_val = 42
        my_sentence = 'Hello, World!'
        
        # This one is to send one value
        # return my_val # This is the equivalent of context['ti'].xcom_push(key='my_key', value=val)
        
        # This one is to send multiple values
        return {
            'my_val': my_val,
            'my_sentence': my_sentence
        }
    
    @task
    def t2(data: Dict[str, Any]): # context: Context
        # val = context['ti'].xcom_pull(task_ids='t1', key='my_key')
        print(data['my_val'])
        print(data['my_sentence'])

    val = t1() 
    t2(val) # This is where it's shared

xcom_dag()