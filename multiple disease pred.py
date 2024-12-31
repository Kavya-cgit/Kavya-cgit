# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:07:06 2024

@author: kanik
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/kanik/OneDrive/Desktop/Multiple Disease Prediction System/saved model/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/kanik/OneDrive/Desktop/Multiple Disease Prediction System/saved model/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/kanik/OneDrive/Desktop/Multiple Disease Prediction System/saved model/parkinsons_model.sav','rb'))


page_bg="""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.news-medical.net/news/20240405/New-machine-learning-model-achieves-breakthrough-in-heart-disease-prediction-with-over-9525-accuracy.aspx");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
                
    }

[data-testid="stSidebar"] {
    background-color: rgba(240, 242, 246, 0.9); /* Light transparent background for sidebar */
            }
h1 {
    font-family: 'Lato', sans-serif;
    color: #4CAF50;  /* Customize color if needed */
    font-size: 40px;  /* Adjust the font size */
    text-align: center;
    }
[data-testid="stSidebar"] {
    background-color: rgba(240, 242, 246, 0.9);
    border-radius: 10px;
    padding: 15px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}


h4 {
    font-family: 'Lato', sans-serif;
    color: #507f7c;
}

button {
    background-color: #2e4053 ;
    color: white;
    border-radius: 5px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #6591a8;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.stButton>button {
    color:#4CAF50;
    width: 100%;
}

.stNumberInput input:focus {
    border-color: #4CAF50 !important;  /* Apply green border on focus */
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.7) !important;  /* Green glow effect */
    outline: none !important;  /* Remove default focus outline */
    transition: all 0.3s ease;  /* Smooth transition for focus effect */
}


.stColumns>div {
    padding: 10px;
}

        
    </style>
    """
st.markdown(page_bg, unsafe_allow_html=True)
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(' Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0,
                           menu_icon="cast",
                           styles={
                               "container": {"padding": "5px", "background-color": "#9ec7c4"},
                               "icon": {"color": "white", "font-size": "20px"},
                               "nav-link": {
                                   "font-size": "16px",
                                   "text-align": "left",
                                   "margin": "0px",
                                   "--hover-color": "#eee",
                               },
                               "nav-link-selected": {"background-color": "#6591a8"},
                         },
                    )

if selected == 'Diabetes Prediction':

   
    st.title('🩺 Diabetes Prediction using ML')
    st.markdown("---")
    st.markdown("<h4 style='color:#507f7c;'>Enter the following details:</h4>", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)

    with col1:
       Pregnancies = st.number_input('Number of Pregnancies',min_value=0, step=1)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0, format="%.2f")

    with col3:
        BMI = st.number_input('BMI value', min_value=0.0, format="%.2f")

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.2f")

    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1)

    # Prediction logic
    diab_diagnosis = ''
    if st.button('Predict Diabetes', key='diabetes_button'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = '🩸 The person is diabetic'
            else:
                diab_diagnosis = '✅ The person is not diabetic'
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    st.markdown("---")
    st.success(diab_diagnosis)


if selected == 'Heart Disease Prediction':

   
    st.title('💖 Heart Disease Prediction using ML')
    st.markdown("---")
    st.markdown("<h4 style='color: #e01e10;'>Enter the following details:</h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=0, step=1)

    with col2:
        sex = st.selectbox('Sex', [0, 1])

    with col3:
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, step=1)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)

    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', min_value=0, max_value=1, step=1)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results (0-2)', min_value=0, max_value=2, step=1)

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)

    with col3:
        exang = st.number_input('Exercise Induced Angina (1 = Yes, 0 = No)', min_value=0, max_value=1, step=1)

    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, format="%.1f")

    with col2:
        slope = st.number_input('Slope of the Peak Exercise ST Segment (0-2)', min_value=0, max_value=2, step=1)

    with col3:
        ca = st.number_input('Number of Major Vessels (0-4)', min_value=0, max_value=4, step=1)

    with col1:
        thal = st.number_input('Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', min_value=0, max_value=2, step=1)

    # Prediction logic
    heart_diagnosis = ''
    if st.button('Predict Heart Disease', key='heart_button' ):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = '💔 The person has heart disease'
            else:
                heart_diagnosis = '✅ The person does not have heart disease'
        except Exception as e:
            st.error(f"An error occurred: {e}")

    st.markdown("---")
    st.success(heart_diagnosis)


if selected == "Parkinsons Prediction":

 
    st.title("🦠 Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)',min_value=0, step=1)

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)',min_value=0, step=1)

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)',min_value=0, step=1)

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)',min_value=0, step=1)

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)',min_value=0, step=1)

    with col1:
        RAP = st.number_input('MDVP:RAP',min_value=0, step=1)

    with col2:
        PPQ = st.number_input('MDVP:PPQ',min_value=0, step=1)

    with col3:
        DDP = st.number_input('Jitter:DDP',min_value=0, step=1)

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer',min_value=0, step=1)

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)',min_value=0, step=1)

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3',min_value=0, step=1)

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5',min_value=0, step=1)

    with col3:
        APQ = st.number_input('MDVP:APQ',min_value=0, step=1)

    with col4:
        DDA = st.number_input('Shimmer:DDA',min_value=0, step=1)

    with col5:
        NHR = st.number_input('NHR',min_value=0, step=1)

    with col1:
        HNR = st.number_input('HNR',min_value=0, step=1)

    with col2:
        RPDE = st.number_input('RPDE',min_value=0, step=1)

    with col3:
        DFA = st.number_input('DFA',min_value=0, step=1)

    with col4:
        spread1 = st.number_input('spread1',min_value=0, step=1)

    with col5:
        spread2 = st.number_input('spread2',min_value=0, step=1)

    with col1:
        D2 = st.number_input('D2',min_value=0, step=1)

    with col2:
        PPE = st.number_input('PPE',min_value=0, step=1)

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button('Predict Parkinsons'):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = " ❌ The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = " ✅ The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
