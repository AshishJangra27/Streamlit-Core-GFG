import time
import numpy as np
import pandas as pd
import streamlit as st

# Static
tab1, tab2 , tab3 = st.tabs(['Cat', 'Dog','Owl'])
tab1.image('https://static.streamlit.io/examples/cat.jpg', width = 200)
tab2.image('https://static.streamlit.io/examples/dog.jpg', width = 200)
tab3.image('https://static.streamlit.io/examples/owl.jpg', width = 200)

# Dynamic

imgs = pd.read_csv('/Users/ashishzangra/Documents/Streamlit/imgs.csv')['img_link']

tabs = st.tabs(["ID"]*30)
for tab in tabs:
    img = imgs[np.random.randint(1,1000)]
    tab.image(img, width = 400)
