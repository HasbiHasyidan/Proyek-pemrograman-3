from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_etl():
    subprocess.run(["spark-submit", "/jobs/etl.py"])

def run_ml():
    subprocess.run(["spark-submit", "/jobs/ml_model.py"])

def generate_graph():
    subprocess.run(["python", "/visualizations/generate_graph.py"])

with DAG(
    "financial_analysis",
    default_args={"start_date": datetime(2023, 11, 1)},
    schedule_interval="@daily",
) as dag:
    etl_task = PythonOperator(
        task_id="etl_task", python_callable=run_etl
    )
    ml_task = PythonOperator(
        task_id="ml_task", python_callable=run_ml
    )
    graph_task = PythonOperator(
        task_id="graph_task", python_callable=generate_graph
    )

    etl_task >> ml_task >> graph_task
