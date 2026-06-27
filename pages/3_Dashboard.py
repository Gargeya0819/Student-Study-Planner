import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from translations import translations
from language import tr

t = translations[st.session_state.language]

st.title("📊 " + tr("dashboard"))
conn = sqlite3.connect("studyplanner.db")

subjects = pd.read_sql_query("SELECT * FROM subjects", conn)

tasks = pd.read_sql_query("SELECT * FROM tasks", conn)

conn.close()

total_subjects = len(subjects)
total_tasks = len(tasks)

completed_tasks = len(tasks[tasks["status"] == "Completed"])

pending_tasks = len(tasks[tasks["status"] == "Pending"])

col1, col2 = st.columns(2)

with col1:
    st.metric(tr("subjects"), total_subjects)

    st.metric(tr("completed_tasks"), completed_tasks)

with col2:
    st.metric(tr("total_tasks"), total_tasks)

    st.metric(tr("pending_tasks"), pending_tasks)

if total_tasks > 0:
    progress = completed_tasks / total_tasks

    st.subheader(tr("overall_progress"))

    st.progress(progress)

    st.write(f"{progress * 100:.1f}% Complete")

st.subheader(tr("task_overview"))

st.dataframe(tasks, use_container_width=True)

st.subheader(tr("task_status_distribution"))

status_counts = tasks["status"].value_counts().reset_index()

status_counts.columns = ["Status", "Count"]

fig = px.pie(
    status_counts, names="Status", values="Count", title="Task Completion Status"
)

st.plotly_chart(fig, use_container_width=True)

pending = tasks[tasks["status"] == "Pending"]

if not pending.empty:
    nearest_task = pending.sort_values("deadline").iloc[0]

    st.warning(
        f"⚠ Upcoming Deadline: "
        f"{nearest_task['task_name']} "
        f" ({nearest_task['deadline']})"
    )
st.subheader("📚 " + tr("subject_wise_workload"))

subject_counts = tasks["subject"].value_counts().reset_index()

subject_counts.columns = ["Subject", "Tasks"]

fig2 = px.bar(subject_counts, x="Subject", y="Tasks", title="Tasks per Subject")

st.plotly_chart(fig2, use_container_width=True)
