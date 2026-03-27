import streamlit as st 
import joblib
import numpy as np 

scaler = joblib.load("scaler-2.pkl")
model = joblib.load("best_model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction")

st.divider()

Age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)
Tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
MonthlyCharges = st.number_input("Enter MonthlyCharges", min_value=30, max_value=150, value=50)
Gender = st.selectbox("Enter the Gender", ["Male", "Female"])

st.divider()

predictbutton = st.button("Predict")

if predictbutton:
    Gender_selected = 1 if Gender == "Female" else 0
    
    x = [Age, Gender_selected, Tenure, MonthlyCharges]
    x_array = scaler.transform([x])
    
    prediction = model.predict(x_array)[0]

    predicted = "Yes" if prediction == 1 else "No"

    st.success(f"Prediction: {predicted}")