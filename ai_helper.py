import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(question):

    prompt = f"""
You are a study planner assistant.

Help students prepare for exams.

Give:
- Important topics
- Study plan
- Revision strategy
- Practical advice

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text
