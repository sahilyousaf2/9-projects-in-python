import streamlit as st

st.set_page_config(page_title="Python-Website", layout="wide")

# web page title and description
st.title("Welcome to my quick streamlit website")
st.write("This is a simple website built in 15 minutes using Streamlit.")

#user input 
name = st.text_input("Enter your name: ")

if name:
    st.write(f'<p style="color:green;">Hello, {name}! Welcome to the streamlit website!<p/>', unsafe_allow_html=True )
    
    
if st.button("Click me!👇 "):
    st.write(f'<p style="color:red;">Waoo, You Clicked the button!<p/>', unsafe_allow_html=True)
    
# user selection for fav color
st.subheader("Select your favourite color 🧮")

color = st.selectbox("Choose a color: ", ['red', 'purple', 'green', 'blue', 'yellow'])

if color:
    st.write(f'<p style="color:{color.lower()}">Your Favourite Color is {color}<p/>', unsafe_allow_html=True)