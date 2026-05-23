import streamlit as st
import requests

st.set_page_config(page_title="Income Classifier", layout="centered")

st.title("💰 Adult Income Prediction System")
st.write("Enter the details below to check if the individual's income is >50K or <=50K.")

# Form banana taake saara data aik sath submit ho
with st.form("prediction_form"):
    st.subheader("Personal & Professional Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=30)
        workclass = st.selectbox("Workclass", ['Private', 'Local-gov', 'Self-emp-not-inc', 'Federal-gov', 'State-gov', 'Self-emp-inc', 'Without-pay', 'Never-worked'])
        fnlwgt = st.number_input("Final Weight (fnlwgt)", min_value=1, value=200000)
        education = st.selectbox("Education", ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-col', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th'])
        education_num = st.number_input("Education Number", min_value=1, max_value=16, value=10)
        marital_status = st.selectbox("Marital Status", ['Married-civ-spouse', 'Never-married', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'])
        occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])

    with col2:
        relationship = st.selectbox("Relationship", ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
        race = st.selectbox("Race", ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
        gender = st.selectbox("Gender", ['Female', 'Male'])
        capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
        capital_loss = st.number_input("Capital Loss", min_value=0, value=0)
        hours_per_week = st.number_input("Hours per Week", min_value=1, max_value=100, value=40)
        native_country = st.selectbox("Native Country", ['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'South', 'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran', 'Philippines', 'Italy', 'Poland', 'Columbia', 'Cambodia', 'Thailand', 'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal', 'Dominican-Republic', 'El-Salvador', 'France', 'Guatemala', 'China', 'Japan', 'Yugoslavia', 'Peru', 'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago', 'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary', 'Holand-Netherlands'])

    # Submit button
    submit_btn = st.form_submit_button("Predict Income")

# Jab user button dabaaye
if submit_btn:
    # FastAPI ka data format tayar karein
    payload = {
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "education_num": education_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }
    
    try:
        # FastAPI server ko request bhejna (Localhost port 8000 par)
        with st.spinner("Calculating prediction..."):
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            response_data = response.json()
            
        # Result display karna
        prediction_result = response_data["prediction"]
        
        if prediction_result == ">50K":
            st.success(f"🎉 Predicted Income is **{prediction_result}** (High Income)")
        else:
            st.warning(f"📊 Predicted Income is **{prediction_result}** (Low Income)")
            
    except Exception as e:
        st.error("Error: Backend not connected. Please make sure the FastAPI server is running")
        