import streamlit as st
from translations import translations


def tr(key):
    lang = st.session_state.get("language", "English")
    return translations.get(lang, {}).get(key, key)
