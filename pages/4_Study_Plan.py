import streamlit as st
import sqlite3
import pandas as pd

from scheduler import generate_schedule
from language import tr

st.title("📅 " + tr("study_plan_generator"))

study_hours = st.number_input(
    tr("available_study_hours"),
    min_value=1,
    max_value=12,
    value=3
)

conn = sqlite3.connect("studyplanner.db")

tasks = pd.read_sql_query(
    """
    SELECT *
    FROM tasks
    WHERE status='Pending'
    """,
    conn
)

conn.close()

if st.button(tr("generate_plan")):

    task_list = tasks.to_dict(
        orient="records"
    )

    schedule = generate_schedule(
        task_list,
        study_hours
    )

    st.subheader(tr("today_study_plan"))

    st.dataframe(
        pd.DataFrame(schedule),
        use_container_width=True
    )
