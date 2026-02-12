FROM apache/airflow:3.0.0

RUN pip install \
    apache-airflow-providers-amazon