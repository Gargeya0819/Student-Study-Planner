from database import initialize_database

initialize_database()

import streamlit as st

st.set_page_config(
    page_title="Student Study Planner",
    page_icon="📚",
    layout="wide"
)

dashboard = st.Page(
    "pages/3_Dashboard.py",
    title="Dashboard",
    icon="📊",
    default=True
)

subjects = st.Page(
    "pages/1_Subjects.py",
    title="Subjects",
    icon="📚"
)

tasks = st.Page(
    "pages/2_Tasks.py",
    title="Tasks",
    icon="📝"
)

study_plan = st.Page(
    "pages/4_Study_Plan.py",
    title="Study Plan",
    icon="📅"
)

weekly_plan = st.Page(
    "pages/5_Weekly_Plan.py",
    title="Weekly Plan",
    icon="🗓️"
)

pg = st.navigation([
    dashboard,
    subjects,
    tasks,
    study_plan,
    weekly_plan
])

pg.run()
