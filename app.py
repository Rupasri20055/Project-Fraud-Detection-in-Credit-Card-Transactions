import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load('xgboost_model.pkl')

st.title("Credit Card Fraud Detection")

uploaded_file = st.file_uploader("Upload transaction data (CSV with same structure as original):", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Assuming scaled_time and scaled_amount are needed
    if 'Time' in data.columns and 'Amount' in data.columns:
        data['scaled_time'] = (data['Time'] - data['Time'].min()) / (data['Time'].max() - data['Time'].min())
        data['scaled_amount'] = (data['Amount'] - data['Amount'].min()) / (data['Amount'].max() - data['Amount'].min())
        data.drop(['Time', 'Amount'], axis=1, inplace=True)

    prediction = model.predict(data)
    st.write("🔍 Prediction Results:")
    st.write(pd.DataFrame({'Prediction': prediction}))
