import streamlit as st
import sqlite3
import pandas as pd
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.title("📝 " + t["tasks"])

conn = sqlite3.connect("studyplanner.db")

subjects = pd.read_sql_query("SELECT name FROM subjects", conn)

subject_list = subjects["name"].tolist()

subject = st.selectbox(t["subject_name"], subject_list)

task_name = st.text_input(t["task_name"])

task_type = st.selectbox(t["task_type"], ["Exam", "Assignment", "Revision"])

deadline = st.date_input(t["deadline"])

if st.button(t["add_task"]):
    cur = conn.cursor()

    cur.execute(
        """
    INSERT INTO tasks
    (subject,task_name,deadline,status)
    VALUES (?,?,?,?)
    """,
        (subject, f"{task_type}: {task_name}", str(deadline), "Pending"),
    )

    conn.commit()

    st.success(t["add_task"])

df = pd.read_sql_query("SELECT * FROM tasks", conn)

st.subheader(t["all_tasks"])

st.dataframe(df, use_container_width=True)

st.subheader("Mark Task Complete")

task_ids = df["id"].tolist()

if task_ids:
    selected_task = st.selectbox("Select Task ID", task_ids)

    if st.button("Complete Task"):
        conn = sqlite3.connect("studyplanner.db")

        cur = conn.cursor()

        cur.execute(
            """
            UPDATE tasks
            SET status='Completed'
            WHERE id=?
            """,
            (selected_task,),
        )

        conn.commit()
        conn.close()

        st.success("Task Completed")

        st.rerun()

st.subheader("Delete Task")

task_ids_delete = df["id"].tolist()

if task_ids_delete:
    delete_task = st.selectbox("Select Task ID to Delete", task_ids_delete)

    if st.button("Delete Task"):
        conn = sqlite3.connect("studyplanner.db")

        cur = conn.cursor()

        cur.execute(
            """
            DELETE FROM tasks
            WHERE id=?
            """,
            (delete_task,),
        )

        conn.commit()
        conn.close()

        st.success("Task Deleted")

        st.rerun()

conn.close()
