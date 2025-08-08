import streamlit as st

st.title("BMI Calculator")

st.write("Welcome! Use the inputs below to calculate your Body Mass Index (BMI).")

# Created number inputs for weight and height to get user inputs.
weight = st.number_input("Enter your weight in kg:", min_value=1.0, max_value=400.0, step=0.5)
height_cm = st.number_input("Enter your height in cm:", min_value=50.0, max_value=400.0, step=0.5)

# Calculate BMI
if weight and height_cm:
    height_m = height_cm / 100 # converts height to meters
    bmi = weight / (height_m ** 2)

    # Categorize BMI according to WHO Standards
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Personalised message for next steps to take
    if category == "Underweight":
        action_to_take = "You are underweight. Eating more can help you reach a healthier BMI range"
    elif category == "Normal Weight":
        action_to_take = "You are normal weight. Keep up your current lifestyle if you have no plans to lose or gain weight."
    elif category == "Obese":
        action_to_take = "You are obese. Consider eating healthier and increasing your physical activity."
    elif category == "Overweight":
        action_to_take = "You are overweight. Losing some weight can help you reach a healthier BMI range."

    # Display result
    st.subheader("Your BMI Results:")
    st.write(f"**BMI:** {bmi:.2f}. You are {category}!") # round the bmi figure to 2 decimal places
    st.write(f"**NEXT STEP:** {action_to_take}")


