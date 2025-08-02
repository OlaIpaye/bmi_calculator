# Building a BMI Calculator

# STEPS:
# 1. Ask user for weight in kg
# 2. Ask user for height in cm
# 3. Convert height to meters
# 4. Calculate BMI
# 5. Categorize BMI
# 6. Display result

# Declaring variables for weight and height
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# Converting height from cm to meters
height_m = height_cm / 100

# Calculating BMI
bmi = weight / (height_m ** 2)

# Categorizing BMI using if-elif-else statements
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 24.9 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Displaying the result
print(f"Your BMI is: {bmi:.2f}. You are classified as: {category}.")
