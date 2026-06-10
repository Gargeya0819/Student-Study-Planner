import streamlit as st
import sqlite3
import pandas as pd

st.title("📚 Subject Management")

subject = st.text_input("Subject Name")

difficulty = st.slider(
    "Difficulty",
    1,
    5,
    3
)

if st.button("Add Subject"):

    conn = sqlite3.connect("studyplanner.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO subjects(name,difficulty)
    VALUES (?,?)
    """, (subject, difficulty))

    conn.commit()
    conn.close()

    st.success("Subject Added")

conn = sqlite3.connect("studyplanner.db")

df = pd.read_sql_query(
    "SELECT * FROM subjects",
    conn
)

conn.close()

st.subheader("All Subjects")

st.dataframe(df, use_container_width=True)
