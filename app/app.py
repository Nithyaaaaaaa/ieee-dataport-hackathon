import streamlit as st

st.set_page_config(page_title="Healthcare Risk Prediction", layout="wide")

st.title("🏥 AI Healthcare Risk Prediction")

st.write("Predict patient disease risk using AI.")

age = st.number_input("Age", 18, 100)

gender = st.selectbox("Gender", ["Male","Female"])

smoking = st.selectbox("Smoking", ["Never","Former","Current"])

diabetes = st.selectbox("Diabetes", ["No","Yes"])

hypertension = st.selectbox("Hypertension", ["No","Yes"])

heart_rate = st.number_input("Average Heart Rate")

bp = st.number_input("Average Systolic BP")

temp = st.number_input("Average Temperature")

spo2 = st.number_input("Average SpO₂")

if st.button("Predict"):
    st.success("Prediction will appear here.")