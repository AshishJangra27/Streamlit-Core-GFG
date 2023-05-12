import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader('Data Visualization with Seaborn and Matplotlib')

st.text('1. Displaying the Dataset')
df = pd.read_csv('/Users/ashishzangra/Documents/Streamlit/iris.csv')
st.dataframe(df)

st.text('2. Bar Plot using Matplotlib')
fig = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.text('3. DistPlot with Seaborn')
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)


st.text('4. Display Multiple Graphs')
col1 , col2 = st.columns(2)
with col1:
    col1.write('KDE = False')
    fig1 = plt.figure()
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.write('Hist = False')
    fig2 = plt.figure()
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.text('5. Changing the Style of the Graphs')
col1 , col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig2)

st.text('6. Scatter Plot')
fig,ax = plt.subplots(figsize  = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.text('7. Count Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)

st.text('8. Box Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.text('9. Violin Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)
