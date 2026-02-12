# from airflow.sdk import dag, task
# from datetime import datetime

# @dag(
#     dag_id="sql_dag",
#     start_date=datetime(2026, 1, 1),
#     schedule=None,
#     catchup=False,
# )
# def sql_dag():
    
#     @task.sql(
#         conn_id='postgres',
#     )
#     def get_nb_xcoms():
#         return 'SELECT COUNT(*) FROM xcom'
    
#     get_nb_xcoms()

# sql_dag()