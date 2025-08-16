import streamlit as st
st.title('BMI Calculator')
st.subheader("This app calculates the bmi based on your data")
# min_ value , max_value, value
weight = st. number_input("Enter your weight (kg)", value =1.0)
height = st. number_input("Enter your height (cms)", value =1.0)

height = height /100

if st. button('Calculate BMI'):
    bmi = weight/ (height ** 2)
    bmi = round (bmi, 2)
    bmi_status = ""
    if bmi < 18.5:
        bmi_status = "underweight"
        st.error(f"you are {bmi_status}")
    elif bmi >= 18.5 and bmi <=24.9:
        bmi_status ="normal"
        st. success(f"you are {bmi_status}")
    elif bmi >= 24.2 and bmi <= 29.9:
        bmi_status ="overweight"
        st.warning(f"you are {bmi_status}")
    else:
        bmi_status = "obese"
        st.error(f"you are {bmi_status}")
