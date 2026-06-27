import streamlit as st
import sqlite3
import pandas as pd
from scheduler import generate_schedule
from language import tr

st.title("📅 " + tr("weekly_study_planner"))

study_hours = st.number_input(
    tr("study_hours_per_day"), min_value=1, max_value=12, value=3
)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

conn = sqlite3.connect("studyplanner.db")

tasks = pd.read_sql_query(
    """
    SELECT *
    FROM tasks
    WHERE status='Pending'
    """,
    conn,
)

conn.close()

if st.button(tr("generate_weekly_plan")):
    task_list = tasks.to_dict(orient="records")

    schedule = generate_schedule(task_list, study_hours)

    st.subheader(tr("weekly_schedule"))

    for day in days:
        st.markdown(f"### {day}")

        for task in schedule:
            st.info(f"{task['subject']} → {task['hours']} hrs")
