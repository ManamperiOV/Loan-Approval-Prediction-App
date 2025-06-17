import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoders
model = joblib.load("saved_models/logistic_regression_model.joblib")
label_encoders = joblib.load("saved_models/label_encoders.joblib")

st.title("🏠 Loan Approval Prediction App")
st.markdown("Fill in the information below to see if your loan would be approved.")

# User input form
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])
applicant_income = st.number_input("Applicant Income (monthly)", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income (monthly)", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", ["Yes", "No"])

# Process input
if st.button("Predict Loan Approval"):
    input_dict = {
        'Gender': label_encoders['Gender'].transform([gender])[0],
        'Married': label_encoders['Married'].transform([married])[0],
        'Dependents': label_encoders['Dependents'].transform([dependents])[0],
        'Education': label_encoders['Education'].transform([education])[0],
        'Self_Employed': label_encoders['Self_Employed'].transform([self_employed])[0],
        'Property_Area': label_encoders['Property_Area'].transform([property_area])[0],
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': 1.0 if credit_history == "Yes" else 0.0
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Not Approved.")