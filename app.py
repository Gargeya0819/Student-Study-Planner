from translations import translations
from database import initialize_database
from language import tr
import streamlit as st

initialize_database()

if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.sidebar.selectbox("Language", ["English", "Telugu"])

st.session_state.language = language

t = translations[language]

st.set_page_config(
    page_title="Student Study Planner",
    page_icon="📚",
    layout="wide",
)

dashboard = st.Page(
    "pages/3_Dashboard.py", title=tr("dashboard"), icon="📊", default=True
)

subjects = st.Page("pages/1_Subjects.py", title=tr("subjects"), icon="📚")

tasks = st.Page("pages/2_Tasks.py", title=tr("tasks"), icon="📝")

study_plan = st.Page("pages/4_Study_Plan.py", title=tr("study_plan"), icon="📅")

weekly_plan = st.Page("pages/5_Weekly_Plan.py", title=tr("weekly_plan"), icon="🗓️")

ai_assistant = st.Page("pages/6_AI_Assistant.py", title=tr("ai_assistant"), icon="🤖")

pg = st.navigation([dashboard, subjects, tasks, study_plan, weekly_plan, ai_assistant])

pg.run()
