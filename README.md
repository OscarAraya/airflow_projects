# airflow_projects
Some airflow projects (learning purposes)


Step 1: Create a Python environment, in this case I used UV (https://docs.astral.sh/uv/) to do so.

uv venv --python 3.11 to create the environment
source .venv/bin/activate to activate it

uv pip install apache-airflow==3.0.0 to install airflow 3.0.0


During the project, I used the Astronomer Registry to check for different Airflow Hooks (https://registry.astronomer.io)

e.g: apache-airflow-providers-provider_name==version

Postgres Hook: uv pip install apache-airflow-providers-postgres==6.1.3

Materialize an Asset to create dependencies: 

Scheduler -> Airflow CLI(bin/bash) -> airflow assets materialize --name assets_name
