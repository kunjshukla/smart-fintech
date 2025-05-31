import streamlit as st
import pandas as pd
from app.main import run_financial_analysis

st.title("SmartFin Advisor")

# File upload
uploaded_file = st.file_uploader("Upload your transaction data (CSV)", type="csv")
risk_profile = st.selectbox("Select your risk profile", ["low", "moderate", "high"])

if uploaded_file and risk_profile:
    # Save the uploaded file
    with open("data/transactions.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Run analysis
    result = run_financial_analysis("data/transactions.csv", risk_profile)
    
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Budget Summary")
        st.write(result["budget_summary"])
        
        st.subheader("Investment Advice")
        st.write(result["investment_advice"])
        
        st.subheader("Fraud Alerts")
        st.write(result["fraud_alerts"])
        
        st.subheader("Financial Report")
        st.write(result["report"])