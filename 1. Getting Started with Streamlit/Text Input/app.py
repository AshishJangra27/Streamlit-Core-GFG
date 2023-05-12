import streamlit as st
from datetime import datetime

st.subheader('1. Text Input')
name = st.text_input('Enter your name : ', value = 'Ashish Jangra')
st.write('Hello',name)

st.subheader('2. Password Input')
password = st.text_input('Enter your password : ',type = 'password', help = 'Atleast have 8 characters')

st.subheader('3. Text Area')
st.text_area('Tell me something about yourself in 200 words', height = 200, max_chars = 500, help = 'Maximum 500 characters allowed')

st.subheader('4. Numeric Input')
st.number_input('Enter your age : ', min_value = 0, max_value = 110, step = 1, value = 24)


st.subheader('5. Date Input')
today = datetime.now().date()
date = st.date_input('Enter the date : ', value = today, min_value = today, max_value = today.replace(year = today.year + 1))
st.write("You've selected : ", datetime.strftime(date, '%d/%m/%Y'))
