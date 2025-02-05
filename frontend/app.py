# frontend/app.py

import streamlit as st
import requests

st.title("FastAPI and Streamlit App")

# FastAPI endpoint URL
url = "http://127.0.0.1:8000/items/"

# Input fields for item creation
name = st.text_input("Item Name")
description = st.text_area("Item Description")

if st.button("Create Item"):
    if name and description:
        response = requests.post(url, json={"name": name, "description": description})
        if response.status_code == 200:
            st.success(f"Item created: {response.json()}")
        else:
            st.error("Failed to create item")
    else:
        st.error("Please fill in all fields.")
