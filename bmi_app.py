
# Functions for the app core logic
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_health_message(category):
    if category == "Underweight":
        return "You are underweight. Eating more can help you reach a healthier BMI range."
    elif category == "Normal Weight":
        return "You are normal weight. Keep up your current lifestyle if you have no plans to lose or gain weight."
    elif category == "Overweight":
        return "You are overweight. Losing some weight can help you reach a healthier BMI range."
    elif category == "Obese":
        return "You are obese. Consider eating healthier and increasing your physical activity."


# Streamlit App

import streamlit as st

st.title("Ola's BMI Calculator")

st.write("Welcome! Use the inputs below to calculate your Body Mass Index (BMI).")

# Created number inputs for weight and height to get user inputs.
weight = st.number_input("Enter your weight in kg:", min_value=1.0, max_value=400.0, step=0.5)
height_cm = st.number_input("Enter your height in cm:", min_value=50.0, max_value=400.0, step=0.5)


if weight and height_cm:
    bmi = calculate_bmi(weight, height_cm) # Calculate BMI
    category = get_bmi_category(bmi) # Categorize BMI
    action_to_take = get_health_message(category) # Friendly health tip to users based on thier categories

    # Display result
    st.subheader("Your BMI Results:")
    st.write(f"**BMI:** {bmi:.2f}. You are {category}!")

    # Show tone-based message based on category
    if category == "Normal Weight":
        st.success(action_to_take)
    elif category == "Underweight":
        st.info(action_to_take)
    elif category == "Overweight":
        st.warning(action_to_take)
    elif category == "Obese":
        st.error(action_to_take)

