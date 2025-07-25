# 🏥 ML Premium Prediction - Healthcare Insurance Premium Prediction App

This is a **machine learning project** built to predict the **annual premium amount** for a healthcare insurance plan based on user-provided inputs.

---

## 📌 Project Objective

The goal of this app is to estimate the insurance premium amount based on personal, medical, and financial details. This helps insurance companies offer more accurate quotes and allows users to understand what factors influence premium costs.

---

## 🌐 Live App

Check out the deployed app on Streamlit here:  
🔗 [ML Premium Prediction App](https://piyush-gala-healthcare-premium-prediction.streamlit.app/)
![Screenshot](assets/ml_premium_prediction_app_ss.png)

---

## 📊 Features Used

The model predicts the premium using the following input features:

| Feature Name            | Description                                                  |
|------------------------|--------------------------------------------------------------|
| `gender`               | Gender of the individual (`Male`, `Female`)            |
| `region`               | Geographic region (`northeast`, `southeast`, `southwest`, `northwest`)         |
| `marital_status`       | Marital status (`Unmarried`, `Married`)                   |
| `bmi_category`         | BMI classification (`Underweight`, `Obesity`, `Normal`, `Overweight`)   |
| `smoking_status`       | Whether the person is a smoker (`Smoker`, `Non-smoker`, `Occasinally`)      |
| `employment_status`    | Employment type (`Salaried`, `Self-employed`, `Freelancer`)          |
| `medical_history`      | Any notable past medical conditions or issues(`Diabetes`, `High blood pressure`, `No Disease`, `Diabetes & High blood pressure`, `Thyroid`, `Heart disease`, `High blood pressure & Heart disease`, `Diabetes & Thyroid`, `Diabetes & Heart disease)`                |
| `insurance_plan`       | Type of insurance plan chosen (`Bronze`, `Silver`, `Gold`)     |
| `age`                  | Age of the applicant in years                                |
| `number_of_dependants` | Number of dependents the person has                          |
| `income_lakhs`         | Annual income in lakhs of INR                                |
| `genetical_risk`       | Indicator of hereditary health risk ranging(0 - 5)            |

---

## 🎯 Target Variable

- **Annual Premium Amount**: The predicted yearly amount an individual will pay for their health insurance.

---

## 🧠 Model Pipeline

1. **Data Preprocessing**:
   - Handling missing values
   - Label encoding for categorical features
   - Standard scaling for numerical features

2. **Exploratory Data Analysis (EDA)**:
   - Correlation heatmaps
   - Distribution plots for features
   - Boxplots to spot outliers

3. **Model Building**:
   - Main algorithm used: **XGBoost Regressor**

4. **Model Evaluation**:
   - Metric used: **R² Score**
   - **Error analysis** done using **residuals percentage** to identify large deviations in prediction vs actual

5. **Deployment**:
   - Deployed using **Streamlit** to allow user interaction with the model via a web app

---

## 🛠️ Technologies Used

- **Python**
- **Pandas, NumPy** – Data processing
- **Matplotlib, Seaborn** – Visualization and EDA
- **Scikit-learn** – Preprocessing utilities and evaluation metrics
- **XGBoost** – ML algorithm used for prediction
- **Streamlit** – Deployment and user interface

---

## 🚀 How to Run the Project Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Piyushgala03/ml-premium-prediction.git
    cd ml-premium-prediction
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

---

## 📩 Contact

For suggestions or feedbacks:

- **Name**: Piyush Gala  
- **LinkedIn**: [Visit My Profile](https://linkedin.com/in/piyush-gala-)

---

