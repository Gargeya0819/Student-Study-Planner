import streamlit as st
from ai_helper import ask_ai
from language import tr

st.title("🤖 " + tr("ai_assistant"))

question = st.text_area(tr("ask_study_advice"), placeholder=tr("ai_placeholder"))

if st.button(tr("get_advice")):
    if question:
        with st.spinner(tr("thinking")):
            response = ask_ai(question)

        st.write(response)
