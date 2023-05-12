import streamlit as st

def bmi_calc():
    st.title("BMI Calculator: ")

    with st.form(key='BMI Calaculator',clear_on_submit = False):
        col1, col2, col3 = st.columns ( [3,2,1])
    with col1:
        weight = st.number_input ("Enter your weight in KGS")
    with col2:
        height = st.number_input("Enter your height in mtrs")
    with col3:
        submit = st.form_submit_button(label = 'Calculate')

    if submit:
        BMI = round((weight / height**2),2)
        if (BMI <= 18.5):
            st.error("Underweight")
        elif(BMI >18.5 and BMI <= 24.9 ):
            st.success ("Healthy/ Normal BMI")
        elif (BMI>=25 and BMI <= 29.9):
            st .warning("Overweight")
        elif (BMI>=30.0):
            st.error ("OBESE")

def rate_yourself():
    with st.sidebar:
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming languages you know with comma sepperation', value = 'Python')
        languages = [i.strip() for i in languages.split(',')]

    st.subheader('How yould you rate your experience in the following programming languages & tools?')

    for language in languages:
        st.write(language)
        st.slider(language, min_value = 0. , max_value = 10., step = .5)

ch = st.sidebar.selectbox("Menu" , ['BMI','Rate Yourself'])

if ch == 'BMI':
    bmi_calc()
elif ch == 'Rate Yourself':
    rate_yourself()
