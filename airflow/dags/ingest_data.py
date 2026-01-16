from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import pandas as pd
import os

# Налаштування
DATA_PATH = '/opt/airflow/data'
PG_CONN_ID = 'postgres_dwh'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

def load_csv_to_postgres(file_name, table_name):
    file_path = os.path.join(DATA_PATH, file_name)
    print(f"Reading file: {file_path}")
    
    # Читання і завантаження
    df = pd.read_csv(file_path)
    hook = PostgresHook(postgres_conn_id=PG_CONN_ID)
    engine = hook.get_sqlalchemy_engine()
    
    with engine.connect() as connection:
        connection.execute(f"TRUNCATE TABLE raw.{table_name}")
        print(f"Table raw.{table_name} truncated.")

    df.to_sql(table_name, engine, schema='raw', if_exists='append', index=False)
    print(f"Loaded {len(df)} rows to {table_name}")

with DAG(
    dag_id='01_ingest_data',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['ingestion']
) as dag:

    load_users = PythonOperator(
        task_id='load_users',
        python_callable=load_csv_to_postgres,
        op_kwargs={'file_name': 'users.csv', 'table_name': 'users'}
    )

    load_orders = PythonOperator(
        task_id='load_orders',
        python_callable=load_csv_to_postgres,
        op_kwargs={'file_name': 'orders.csv', 'table_name': 'orders'}
    )

    load_users >> load_orders