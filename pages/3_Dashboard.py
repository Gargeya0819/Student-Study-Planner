import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard")

conn = sqlite3.connect("studyplanner.db")

subjects = pd.read_sql_query(
    "SELECT * FROM subjects",
    conn
)

tasks = pd.read_sql_query(
    "SELECT * FROM tasks",
    conn
)

conn.close()

total_subjects = len(subjects)
total_tasks = len(tasks)

completed_tasks = len(
    tasks[tasks["status"] == "Completed"]
)

pending_tasks = len(
    tasks[tasks["status"] == "Pending"]
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Subjects",
        total_subjects
    )

    st.metric(
        "Completed Tasks",
        completed_tasks
    )

with col2:
    st.metric(
        "Total Tasks",
        total_tasks
    )

    st.metric(
        "Pending Tasks",
        pending_tasks
    )

if total_tasks > 0:

    progress = completed_tasks / total_tasks

    st.subheader("Overall Progress")

    st.progress(progress)

    st.write(
        f"{progress * 100:.1f}% Complete"
    )

st.subheader("Task Overview")

st.dataframe(tasks, use_container_width=True)

st.subheader("Task Status Distribution")

status_counts = (
    tasks["status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = [
    "Status",
    "Count"
]

fig = px.pie(
    status_counts,
    names="Status",
    values="Count",
    title="Task Completion Status"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

pending = tasks[
    tasks["status"] == "Pending"
]

if not pending.empty:

    nearest_task = (
        pending.sort_values("deadline")
        .iloc[0]
    )

    st.warning(
        f"⚠ Upcoming Deadline: "
        f"{nearest_task['task_name']} "
        f" ({nearest_task['deadline']})"
    )
st.subheader("📚 Subject-wise Workload")

subject_counts = (
    tasks["subject"]
    .value_counts()
    .reset_index()
)

subject_counts.columns = [
    "Subject",
    "Tasks"
]

fig2 = px.bar(
    subject_counts,
    x="Subject",
    y="Tasks",
    title="Tasks per Subject"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
