import time
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(page_title = "GeeksForGeeks", page_icon = '♥️', layout = 'wide')

# Spinner
with st.spinner('Wait for it'):
    time.sleep(5)
    st.write('Thanks for being patient!')

# Progress Bar
with st.empty():
    for percent_completed in range(100):
        time.sleep(.1)
        st.progress(percent_completed + 1, text = 'Processing')
    st.success('Congratulations!')

# Cool Stuf
st.balloons()
st.snow()
