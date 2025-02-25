# -*- coding: utf-8 -*-
"""user_app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-870mHldiZ9svkczmIvpy1jMZH4KKxJk
"""

import streamlit as st
import requests
from datetime import datetime
import os

# Backend URL (Replace with your actual Render URL)
BACKEND_URL = "https://ai-equity-analyst.onrender.com"

st.title("AI Equity Analyst")

# User selects a company
company_name = st.text_input("Enter Company Name")

if st.button("Get Analysis"):
    response = requests.get(f"{BACKEND_URL}/summary/{company_name}")
    if response.status_code == 200:
        summaries = response.json().get("Summaries", [])
        if summaries:
            for summary in summaries:
                st.subheader(f"📅 {summary['Date']} - {summary['Document Type']}")
                st.write(f"📄 **File:** {summary['Filename']}")
                st.write(f"📜 **Summary:** {summary['Summary']}")
                st.markdown("---")
        else:
            st.warning("⚠️ No summaries found for this company.")
    else:
        st.error("❌ Failed to fetch summaries.")