import streamlit as st
import time

st.set_page_config(
    page_title="Python Exam 2024",
    page_icon="🐒",
    layout="wide",
)
st.title("CBS 2024 Python Exam Streamlit Dashboard")

placeholder = st.empty()

with placeholder.container():
    st.markdown("### Student Name: Ziwei Yan ")
    time.sleep(1)