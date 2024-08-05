# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:20:36 2024

@author: Hp
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# Loading the saved models
diabetes_model = pickle.load(open("diabetes_trained_model.sav", "rb"))
heart_model = pickle.load(open("heart_disease_trained_model.sav", "rb"))
parkinsons_model = pickle.load(open("parkinsons_trained_model.sav", "rb"))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction','BMI Calculator'],
                           icons=['activity', 'heart', 'person','calculator-fill'],
                           default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Enter the number of Pregnancies")
    with col2:
        Glucose = st.text_input("Enter the Glucose level")
    with col3:
        BloodPressure = st.text_input("Enter the Blood Pressure level")
    with col1:
        SkinThickness = st.text_input("Enter the Skin Thickness value")
    with col2:
        Insulin = st.text_input("Enter the Insulin level")
    with col3:
        BMI = st.text_input("Enter the BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Enter the Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Enter the Age")
    
    # Code for prediction
    diabetes_diagnosis = ''
    
    # Creating a button
    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diabetes_prediction = diabetes_model.predict([input_data])
            
            if diabetes_prediction[0] == 1:
                diabetes_diagnosis = 'The patient is Diabetic'
            else:
                diabetes_diagnosis = 'The patient is not Diabetic'
        
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    
    st.success(diabetes_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Getting the input data from user
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input("Enter the age of the patient")
    with col2:
        sex = st.text_input("Enter the sex of the patient")
    with col1:
        cp = st.text_input("Enter the chest pain type of the patient")
    with col2:
        trestbps = st.text_input("Enter the resting blood pressure in mm Hg of the patient")
    with col1:
        chol = st.text_input("Enter the serum cholesterol in mg/dl of the patient")
    with col2:
        fbs = st.text_input("Enter the fasting blood sugar of the patient")
    with col1:
        restecg = st.text_input("Enter the resting electrocardiographic results of the patient")
    with col2:
        thalach = st.text_input("Enter the maximum heart rate achieved for the patient")
    with col1:
        exang = st.text_input("Has the patient ever had chest pain or discomfort during exercise or stress that goes away with rest?")
    with col2:
        oldpeak = st.text_input("Has the patient ever had ST depression on an ECG during a stress test?")
    with col1:
        slope = st.text_input("Has the patient ever had an ECG that showed a change in the slope of the ST segment during peak exercise?")
    with col2:
        ca = st.text_input("Enter the number of major vessels (0-3) colored by fluoroscopy for the patient")
    with col1:
        thal = st.text_input("Has a stress test ever shown a fixed defect, reversible defect, or normal result in the 'thal' variable for the patient's heart assessment?")
    
    # Code for prediction
    heart_disease_diagnosis = ''
    
    # Creating a button
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                          float(ca), float(thal)]
            heart_disease_prediction = heart_model.predict([input_data])
            
            if heart_disease_prediction[0] == 1:
                heart_disease_diagnosis = 'The patient has Heart Disease'
            else:
                heart_disease_diagnosis = 'The patient does not have Heart Disease'
        
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    
    st.success(heart_disease_diagnosis)

# Parkinson's Prediction
scaler=StandardScaler()
if selected == 'Parkinsons Prediction':
    # Page title
    st.title('Parkinsons Prediction using ML')
    
    # Getting the input data from user
    col1, col2 = st.columns(2)
    
    with col1:
        MDVP_Fo_Hz = st.text_input("Enter the average vocal fundamental frequency (MDVP:Fo(Hz))")
    with col2:
        MDVP_Fhi_Hz = st.text_input("Enter the maximum vocal fundamental frequency (MDVP:Fhi(Hz))")
    with col1:
        MDVP_Flo_Hz = st.text_input("Enter the minimum vocal fundamental frequency (MDVP:Flo(Hz))")
    with col2:
        MDVP_Jitter_Percent = st.text_input("Enter the measure of variation in fundamental frequency (MDVP:Jitter(%))")
    with col1:
        MDVP_Jitter_Abs = st.text_input("Enter the absolute measure of variation in fundamental frequency (MDVP:Jitter(Abs))")
    with col2:
        MDVP_RAP = st.text_input("Enter the relative amplitude perturbation (MDVP:RAP)")
    with col1:
        MDVP_PPQ = st.text_input("Enter the five-point period perturbation quotient (MDVP:PPQ)")
    with col2:
        Jitter_DDP = st.text_input("Enter the degree of deviation in pitch (Jitter:DDP)")
    with col1:
        MDVP_Shimmer = st.text_input("Enter the measure of variation in amplitude (MDVP:Shimmer)")
    with col2:
        MDVP_Shimmer_dB = st.text_input("Enter the measure of variation in amplitude in decibels (MDVP:Shimmer(dB))")
    with col1:
        Shimmer_APQ3 = st.text_input("Enter the three-point amplitude perturbation quotient (Shimmer:APQ3)")
    with col2:
        Shimmer_APQ5 = st.text_input("Enter the five-point amplitude perturbation quotient (Shimmer:APQ5)")
    with col1:
        MDVP_APQ = st.text_input("Enter the average amplitude perturbation quotient (MDVP:APQ)")
    with col2:
        Shimmer_DDA = st.text_input("Enter the degree of deviation in amplitude (Shimmer:DDA)")
    with col1:
        NHR = st.text_input("Enter the measure of ratio of noise to tonal components in the voice (NHR)")
    with col2:
        HNR = st.text_input("Enter the measure of harmonic to noise ratio (HNR)")
    with col1:
        RPDE = st.text_input("Enter the recurrence period density entropy (RPDE)")
    with col2:
        DFA = st.text_input("Enter the signal fractal scaling exponent (DFA)")
    with col1:
        spread1 = st.text_input("Enter the nonlinear measure of fundamental frequency variation (spread1)")
    with col2:
        spread2 = st.text_input("Enter the nonlinear measure of fundamental frequency variation (spread2)")
    with col1:
        D2 = st.text_input("Enter the nonlinear dynamical complexity measure (D2)")
    with col2:
        PPE = st.text_input("Enter the fundamental frequency variation measure (PPE)")
    
    # Code for prediction
    parkinsons_diagnosis = ''
    
    # Creating a button
    if st.button('Parkinsons Test Result'):
        try:
            input_data = [float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), float(MDVP_Jitter_Percent), 
                          float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP), 
                          float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), 
                          float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE), float(DFA), 
                          float(spread1), float(spread2), float(D2), float(PPE)]
            input_features = scaler.transform([input_data])
            parkinsons_prediction = parkinsons_model.predict(input_features)
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The patient exhibits the sign of Parkinsons'
            else:
                parkinsons_diagnosis = 'The patient does not exhibit the sign of Parkinsons'
        
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    
    st.success(parkinsons_diagnosis)


#BMI Calculator
if (selected=='BMI Calculator'):
    st.title("BMI Calculator")
    
    weight = st.number_input("Enter your weight in kilograms: ")
    height = st.number_input("Enter your height in centimeters: ")
    
    bmi=''
    
    #Create button
    if st.button("BMI Result"):
        bmi = weight / pow((height/100), 2)
        
        if bmi < 18.5:
            result = "Underweight"
        elif 18.5 <= bmi < 24.9:
            result = "Normal weight"
        elif 25 <= bmi < 29.9:
            result = "Overweight"
        else:
            result = "Obesity"
                
        # Display results
        st.success(f"Your BMI is: {bmi:.2f}")
        st.success(f"Your BMI category is: {result}")
    else:
        st.error("Height must be greater than zero.")