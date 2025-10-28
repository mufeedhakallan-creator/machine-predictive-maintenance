import streamlit as st
import pandas as pd
import numpy as np
import joblib
from jinja2.sandbox import unsafe

st.image("machine.jpeg")



model = joblib.load('machine_failure_model1 (2).pkl')
lab_type = joblib.load('lab_type.pkl')
lab_prod = joblib.load('lab_prod.pkl')


st.markdown(
    "<h1 style='color:#2C3539; text-align:centre;'>⚙Machine Failure Prediction </h1>",
    unsafe_allow_html = True
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;  /* Light blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #1E90FF;  /* Green */
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 10em;
        font-size: 16px;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;  /* Darker green on hover */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='color:#4682B4; font-family:Arial; text-align:center;'>
        Enter the Machine Parameters Below 👇
    </h3>
""", unsafe_allow_html=True)



#categorical inputs
type_input = st.selectbox('Machine Types',lab_type.classes_)
product_input = st.selectbox('Product ID',lab_prod.classes_)

#Numeric input
air_temp = st.number_input('Air temperature [k]',min_value=0.0,max_value=1000.0,step=0.1)
process_temp = st.number_input('Process temperature [k]',min_value=0)
rot_speed = st.number_input('Rotational speed [rpm]',min_value=0,max_value=10000,step=1)
torque = st.number_input('Torque [NM]',min_value=0.0,max_value=1000.0,step=0.1)
tool_wear = st.number_input('Tool wear [min]',min_value=0,max_value=500,step=1)
twf = st.number_input('TWF',min_value=0,max_value=1,step=1)
hdf = st.number_input('HDF',min_value=0,max_value=1,step=1)
pwf = st.number_input('PWF',min_value=0,max_value=1,step=1)
osf = st.number_input('OSF',min_value=0,max_value=1,step=1)
rnf = st.number_input('RNF',min_value=0,max_value=1,step=1)

type_encoded = lab_type.transform([type_input])[0]
product_encoded = lab_prod.transform([product_input])[0]

input_data = np.array([[product_encoded,type_encoded,air_temp,process_temp,rot_speed,torque,tool_wear,twf,hdf,
                        pwf,osf,rnf]])


if st.button('Predict Machine Failure'):
    prediction = model.predict(input_data)[0]
    if prediction == 1:

        st.error('⚠  Machine is likely to Fail soon,Please check maintenance')
    else:
        st.success('✅ machine is operating Normally.No immediate issue detected')