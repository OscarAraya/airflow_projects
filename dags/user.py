from airflow.sdk import asset, Asset, Context

@asset(
    #name='user' # It will automatically use the function name
    schedule='@daily',
    uri='https://randomuser.me/api/'
)
def user(self) -> dict[str]:
    import requests

    response = requests.get(self.uri)
    return response.json() # airflow assets list to check the existing assets

# Using the multi method from Asset
@asset.multi(
    schedule=user,
    outlets=[
         Asset(name='user_location'),
         Asset(name='user_login')
    ]
)
def user_info(user: Asset, context: Context) -> dict[str]:
    user_data = context['ti'].xcom_pull(
        dag_id=user.name,
        task_ids=user.name,
        include_prior_dates=True
    )

    return [
        user_data['results'][0]['location'],
        user_data['results'][0]['login']
    ]

# Single method Asset
@asset(
    schedule=user
)
def user_location(user: Asset, context: Context) -> dict[str]:
    user_data = context['ti'].xcom_pull(
        dag_id=user.name,
        task_ids=user.name,
        include_prior_dates=True
    )

    return user_data['results'][0]['location']

@asset(
    schedule=user
)
def user_login(user: Asset, context: Context) -> dict[str]:
    user_data = context['ti'].xcom_pull(
        dag_id=user.name,
        task_ids=user.name,
        include_prior_dates=True
    )

    return user_data['results'][0]['login']