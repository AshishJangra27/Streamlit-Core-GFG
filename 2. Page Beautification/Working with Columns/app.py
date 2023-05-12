import time
import numpy as np
import streamlit as st


# Static
col1, col2, col3 = st.columns(3)
with col1:
    st.header('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg', width = 200)
with col2:
    st.header('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg', width = 200)
with col3:
    st.header('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg', width = 200)


# Dynamic
n = st.number_input('How many columns do you want?', 1,10)
cols = st.columns(n)
for col in cols:
    with col:
        st.image('https://static.streamlit.io/examples/dog.jpg')
