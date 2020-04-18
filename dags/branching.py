import random
from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 5, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



def return_branch(**kwargs):

    branches = ['branch_0', 'branch_1', 'branch_2', 'branch_3', 'branch_4']

    return random.choice(branches)

with DAG(
        "branching",
        start_date=datetime(1992, 1, 1),
        schedule_interval="@yearly",
    ) as dag:

    kick_off_dag = DummyOperator(task_id='run_this_first')

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=return_branch,
        provide_context=True)

    kick_off_dag >> branching

    for i in range(0, 5):
        d = DummyOperator(task_id='branch_{0}'.format(i))
        for j in range(0, 3):
            m = DummyOperator(task_id='branch_{0}_{1}'.format(i, j))

            d >> m

        branching >> d
