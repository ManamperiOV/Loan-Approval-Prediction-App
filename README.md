# 🏠 Loan Approval Prediction App

A machine learning project that predicts whether a loan will be approved based on user-input features like income, credit history, employment status, and more. The final app is deployed using **Streamlit**.

---

## 🚀 Features

- Multiple ML models trained and compared
- Missing value handling
- Label encoding for categorical features
- Model evaluation via confusion matrix
- Final model deployed with Streamlit

---

## 🧠 Problem Statement

Given information about a loan applicant (e.g., income, education, employment status), predict whether the loan will be **approved (1)** or **not approved (0)**.

---

## 📊 Dataset

- **Source**: [Loan Prediction Dataset]([https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset?resource=download))
- **Rows**: 614  
- **Target Variable**: `Loan_Status` (1 = Approved, 0 = Not Approved)

---

## 🔍 Data Preprocessing

- **Missing Values**:
  - Numerical: Filled with median
  - Categorical: Filled with mode
- **Label Encoding**:
  Used `LabelEncoder` to convert categorical features to numeric format
- **Train/Test Split**: 80% training / 20% testing

---

## 🤖 Model Comparison

Several models were trained and tested:

| Model                   | Accuracy |
|------------------------|----------|
| Logistic Regression     | **0.79** ✅ *(Deployed)*  
| K-Nearest Neighbors     | 0.76  
| Support Vector Machine  | 0.79  
| Gradient Boosting       | 0.74  
| XGBoost                 | 0.74  
| Random Forest           | 0.75  

> Confusion matrix showed Logistic Regression had the best balanced performance.

---


---

## 🌐 Streamlit App Overview

### 📝 User Inputs:

- Gender
- Married status
- Dependents
- Education
- Self-Employed
- Applicant Income
- Coapplicant Income
- Loan Amount (in thousands)
- Loan Amount Term (in months)
- Credit History (Yes/No)
- Property Area (Urban, Rural, Semiurban)

### ✅ Output:

- **Prediction**: Approved ✅ or Not Approved ❌
- Uses trained Logistic Regression model
- Encodes inputs using saved label encoders
- Displays result in a user-friendly interface

---

## 🧪 Confusion Matrix

Logistic Regression performance on test set:

![Confusion Matrix](![image](https://github.com/user-attachments/assets/f342cd7d-f6a5-4d0e-b232-b46e21f52ad3)
)

---

## 🖥️ Run the App

```bash
streamlit run loan_approval_app.py

![Screenshot 2025-06-17 163052](https://github.com/user-attachments/assets/38c4e72b-fdc8-4dd0-b3f4-a48bcaf05fcd)
![Screenshot 2025-06-17 163151](https://github.com/user-attachments/assets/b7434216-9137-46d3-a50e-8f310085543e)


