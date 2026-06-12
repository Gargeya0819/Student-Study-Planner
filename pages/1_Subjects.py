import streamlit as st
import sqlite3
import pandas as pd
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.title("📚 " + t["subjects"])

subject = st.text_input(t["subject_name"])

difficulty = st.slider(
    t["difficulty"],
    1,
    5,
    3
)

if st.button(t["add_subject"]):

    conn = sqlite3.connect("studyplanner.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO subjects(name,difficulty)
    VALUES (?,?)
    """, (subject, difficulty))

    conn.commit()
    conn.close()

    st.success(t["add_subject"])

conn = sqlite3.connect("studyplanner.db")

df = pd.read_sql_query(
    "SELECT * FROM subjects",
    conn
)

conn.close()

st.subheader(t["all_subjects"])

st.dataframe(df, use_container_width=True)
