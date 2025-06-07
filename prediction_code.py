import pandas as pd
from joblib import load

model_rest = load('artifacts/model_rest.joblib')
model_young = load('artifacts/model_young.joblib')

scaler_rest = load('artifacts/scaler_rest.joblib')
scaler_young = load('artifacts/scaler_young.joblib')

# Risk score mapping
risk_score = {
    'diabetes': 6,
    'heart disease': 8,
    'high blood pressure': 6,
    'thyroid': 5,
    'no disease': 0,
    'none': 0
}

# Preprocessing function
def preprocess_input(input_dict):
    # Manually encode categorical features using if-else
    gender_Male = 1 if input_dict['gender'] == 'Male' else 0

    region_Northwest = 1 if input_dict['region'] == 'Northwest' else 0
    region_Southeast = 1 if input_dict['region'] == 'Southeast' else 0
    region_Southwest = 1 if input_dict['region'] == 'Southwest' else 0

    marital_status_Unmarried = 1 if input_dict['marital_status'] == 'Unmarried' else 0

    bmi_category_Obesity = 1 if input_dict['bmi_category'] == 'Obesity' else 0
    bmi_category_Overweight = 1 if input_dict['bmi_category'] == 'Overweight' else 0
    bmi_category_Underweight = 1 if input_dict['bmi_category'] == 'Underweight' else 0

    smoking_status_Occasional = 1 if input_dict['smoking_status'] == 'Occasional' else 0
    smoking_status_Regular = 1 if input_dict['smoking_status'] == 'Regular' else 0

    employment_status_Salaried = 1 if input_dict['employment_status'] == 'Salaried' else 0
    employment_status_Self_Employed = 1 if input_dict['employment_status'] == 'Self-Employed' else 0

    # Encode insurance plan
    if input_dict['insurance_plan'] == 'Bronze':
        insurance_plan = 1
    elif input_dict['insurance_plan'] == 'Silver':
        insurance_plan = 2
    elif input_dict['insurance_plan'] == 'Gold':
        insurance_plan = 3
    else:
        insurance_plan = 0  # fallback

    # --- Calculate total_risk_score from medical history ---
    diseases = input_dict['medical_history'].lower().split('&')
    total_risk_score = 0
    for disease in diseases:
        disease = disease.strip()
        total_risk_score += risk_score.get(disease, 0)

    # Final feature vector
    input_data = [[
        input_dict['age'],
        input_dict['number_of_dependants'],
        input_dict['income_lakhs'],
        insurance_plan,
        input_dict['genetical_risk'],
        total_risk_score,
        gender_Male,
        region_Northwest,
        region_Southeast,
        region_Southwest,
        marital_status_Unmarried,
        bmi_category_Obesity,
        bmi_category_Overweight,
        bmi_category_Underweight,
        smoking_status_Occasional,
        smoking_status_Regular,
        employment_status_Salaried,
        employment_status_Self_Employed
    ]]

    # Convert to DataFrame with correct column order
    columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
        'genetical_risk', 'total_risk_score', 'gender_Male', 'region_Northwest',
        'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight',
        'smoking_status_Occasional', 'smoking_status_Regular',
        'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    return pd.DataFrame(input_data, columns=columns)

# Prediction code
def predict(input_dict):
    input_df = preprocess_input(input_dict)

    if input_dict['age'] <= 25:
        scaler_dict = scaler_young  # already loaded as dict
        scaler = scaler_dict['scaler']
        cols_to_scale = scaler_dict['col_to_scale']

        input_df_scaled = input_df.copy()
        input_df_scaled[cols_to_scale] = scaler.transform(input_df[cols_to_scale])
        prediction = model_young.predict(input_df_scaled)

    else:
        scaler_dict = scaler_rest
        scaler = scaler_dict['scaler']
        cols_to_scale = scaler_dict['col_to_scale']

        input_df_scaled = input_df.copy()
        input_df_scaled[cols_to_scale] = scaler.transform(input_df[cols_to_scale])
        prediction = model_rest.predict(input_df_scaled)

    return prediction[0]
