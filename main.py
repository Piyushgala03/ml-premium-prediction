import streamlit as st
from prediction_code import predict

st.title('Health Insurance Premium Prediction App')

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
with col2:
    region = st.selectbox("Region", ["Northwest", "Southeast", "Northeast", "Southwest"])
with col3:
    marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    bmi_category = st.selectbox("BMI Category", ["Normal", "Obesity", "Overweight", "Underweight"])
with col5:
    smoking_status = st.selectbox("Smoking Status", [
        "No Smoking", "Regular", "Occasional"
    ])
with col6:
    employment_status = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Freelancer"])

# Row 3
col7, col8, col9 = st.columns(3)
with col7:
    genetical_risk = st.number_input("Genetical Risk (0 to 5)", min_value=0.0, max_value=5.0, step=1.0)
with col8:
    medical_history = st.selectbox("Medical History", [
        "Diabetes", "High blood pressure", "No Disease",
        "Diabetes & High blood pressure", "Thyroid", "Heart disease",
        "High blood pressure & Heart disease", "Diabetes & Thyroid", "Diabetes & Heart disease"
    ])
with col9:
    insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])

# Row 4
col10, col11, col12 = st.columns(3)
with col10:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with col11:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=20, step=1)
with col12:
    income_lakhs = st.number_input("Income (in Lakhs)", min_value=0, max_value=200, step=1)

input_dict = {
    "gender": gender,
    "region": region,
    "marital_status": marital_status,
    "bmi_category": bmi_category,
    "smoking_status": smoking_status,
    "employment_status": employment_status,
    "medical_history": medical_history,
    "insurance_plan": insurance_plan,
    "age": age,
    "number_of_dependants": number_of_dependants,
    "income_lakhs": income_lakhs,
    "genetical_risk": genetical_risk
}

if st.button('Predict'):
    predicted_val = predict(input_dict)
    st.success(f'Predicted Premium: {predicted_val}')