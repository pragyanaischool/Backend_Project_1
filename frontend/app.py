import streamlit as st
import requests

# 🔗 Replace with your Render URL
API_URL = "https://backend-project-1-1.onrender.com"

st.set_page_config(page_title="FastAPI + Streamlit", layout="centered")

st.title("🚀 FastAPI + Streamlit Frontend")

st.write("Connect to deployed FastAPI backend")

# -----------------------------
# 🔍 Health Check
# -----------------------------
if st.button("Check API Status"):
    try:
        res = requests.get(f"{API_URL}/health", timeout=10)
        st.success(res.json())
    except Exception as e:
        st.error(f"API Error: {e}")

# -----------------------------
# 📡 Get Data from API
# -----------------------------
if st.button("Get Message"):
    try:
        res = requests.get(API_URL, timeout=10)
        st.json(res.json())
    except Exception as e:
        st.error(f"Error: {e}")
