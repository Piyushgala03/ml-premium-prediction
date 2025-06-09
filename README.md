# 🏥 ML Premium Prediction - Healthcare Insurance Premium Prediction App

This is a **machine learning project** built to predict the **annual premium amount** for a healthcare insurance plan based on user-provided inputs. It is a **guided project by [codebasics.io](https://codebasics.io)**, with additional independent experimentation—such as model selection, evaluation, and deployment—done to enhance performance and understanding.

---

## 📌 Project Objective

The goal of this app is to estimate the insurance premium amount based on personal, medical, and financial details. This helps insurance companies offer more accurate quotes and allows users to understand what factors influence premium costs.

---

## 🌐 Live App

Check out the deployed app on Streamlit here:  
🔗 [ML Premium Prediction App](https://piyush-gala-healthcare-premium-prediction.streamlit.app/)

---

## 📊 Features Used

The model predicts the premium using the following input features:

| Feature Name            | Description                                                  |
|------------------------|--------------------------------------------------------------|
| `gender`               | Gender of the individual (`Male`, `Female`, etc.)            |
| `region`               | Geographic region (`north`, `south`, `east`, `west`)         |
| `marital_status`       | Marital status (`Single`, `Married`, etc.)                   |
| `bmi_category`         | BMI classification (`Underweight`, `Normal`, `Overweight`)   |
| `smoking_status`       | Whether the person is a smoker (`Smoker`, `Non-smoker`)      |
| `employment_status`    | Employment type (`Salaried`, `Self-employed`, etc.)          |
| `medical_history`      | Any notable past medical conditions or issues                |
| `insurance_plan`       | Type of insurance plan chosen (`Basic`, `Premium`, etc.)     |
| `age`                  | Age of the applicant in years                                |
| `number_of_dependants` | Number of dependents the person has                          |
| `income_lakhs`         | Annual income in lakhs of INR                                |
| `genetical_risk`       | Indicator of hereditary health risk (`Yes`, `No`)            |

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

## 📚 Credits

This project is part of a guided learning series from [codebasics.io](https://codebasics.io), which helps learners build hands-on data science and machine learning projects. Model selection and deployment were explored independently.

---

## 📩 Contact

For suggestions or feedbacks:

- **Name**: Piyush Gala  
- **LinkedIn**: [LinkedIn Profile](https://linkedin.com/in/piyush-gala-)

---

