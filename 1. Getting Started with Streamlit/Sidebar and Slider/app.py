import streamlit as st

with st.sidebar:
    st.title('Rate Yourself')
    languages = st.text_input('Enter the programming languages you know with comma sepperation', value = 'Python')
    languages = [i.strip() for i in languages.split(',')]

st.subheader('How yould you rate your experience in the following programming languages & tools?')

for language in languages:
    st.write(language)
    st.slider(language, min_value = 0. , max_value = 10., step = .5)
