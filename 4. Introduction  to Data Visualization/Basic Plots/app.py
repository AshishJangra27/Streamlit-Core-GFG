import numpy as np
import pandas as pd
import streamlit as st

# Defining the Dataset
chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['L-1','L-2','L-3'])

# Plotting Line Chart
st.title('1. Line Chart')
st.line_chart(chart_data)

# Plotting Area Chart
st.title('2. Area Chart')
st.area_chart(chart_data)

# Plotting Bar Chart
st.title('3. Bar Chart')
st.bar_chart(chart_data)
