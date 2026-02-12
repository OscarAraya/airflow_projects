# airflow_projects
Some airflow projects (learning purposes)

Step 1: Create a Python environment, in this case I used UV (https://docs.astral.sh/uv/) to do so.

uv venv --python 3.11 to create the environment
source .venv/bin/activate to activate it

uv pip install apache-airflow==3.0.0 to install airflow 3.0.0

Hooks:

During the project, I used the Astronomer Registry to check for different Airflow Hooks (https://registry.astronomer.io)

e.g: apache-airflow-providers-provider_name==version

Postgres Hook: uv pip install apache-airflow-providers-postgres==6.1.3

Assets:

Materialize an Asset to create dependencies: 

Scheduler -> Airflow CLI(bin/bash) -> airflow assets materialize --name assets_name

Celery:

In order to create new Celery workers, you need to modify the docker-compose file to add a new instance of the existing one and changing its name.

Flower:

Use it to monitor Celery, docker compose --profile flower up.

Queues:

In case you need to add different queues, you need to change the command line from the worker in the docker-compose file.

E.g. command: celery worker -q queue_name

Airflow Provider

1. Create a new folder for the provider-name
2. Create a .toml configuration file
