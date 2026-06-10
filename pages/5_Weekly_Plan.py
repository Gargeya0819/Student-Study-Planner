import streamlit as st
import sqlite3
import pandas as pd
from scheduler import generate_schedule

st.title("📅 Weekly Study Planner")

study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=1,
    max_value=12,
    value=3
)

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

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

if st.button("Generate Weekly Plan"):

    task_list = tasks.to_dict(
        orient="records"
    )

    schedule = generate_schedule(
        task_list,
        study_hours
    )

    st.subheader("Weekly Schedule")

    for i, day in enumerate(days):

        st.markdown(f"### {day}")

        for task in schedule:

            st.info(
    f"{task['subject']} → "
    f"{task['hours']} hrs"
)
