import streamlit as st
import time 

st.set_page_config(page_title="BMI Calcuator", layout="wide")

# page title
st.title("BMI Calculator In Python 🧮")

st.markdown("""
            A BMI calculator determines if your weight is within a healthy range based on your height and weight
            """)

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("weight (kg): ", min_value=1.0, format="%.2f")
with col2: 
    height = st.number_input("Height (m): ", min_value=1.0, format="%.2f")
    
if height > 0 and weight > 0:
    bmi = weight / (height ** 2 )  #bmi formula
    st.subheader("Your BMI")
    st.markdown(f"{bmi:.2f}", unsafe_allow_html=True)
    
    if bmi < 18.5: 
        st.error("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9: 
        st.warning("Overweight")
    else:
        st.error("Obsity 🚨")
        
else:
    st.info("Please enter a valid weight and height")