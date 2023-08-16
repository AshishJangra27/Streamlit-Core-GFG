import pandas as pd
import streamlit as st
df = pd.read_csv('/Users/ashishzangra/Desktop/Streamlit/code/abalone.csv')

st.subheader ('1. Displaying the whole DataFrame')
st.dataframe (df)

st.subheader('2. Displaying the head of DataFrame')
st.dataframe (df.head())

st.subheader('3. Displaying the tail of DataFrame')
st.dataframe(df.tail ())

st.subheader('4. Displaying in a Table(first 20 rows) ')
st.table(df.head(20))

st.subheader ('5. Displaying JSON')
st.json([{'pid': 1, 'name': '5 Star'},
        {'pid' : 2, 'name' : 'Milky-Bar'},
        {'pid' : 3, 'name' : 'Multigrain Bread'},
        {'pid' : 4, 'name' : 'Butter'},
        {'pid': 5, 'name' : 'Dairy Milk'}])
st.subheader ('6. Displaving the Description of Data')
st.table(df.describe())
