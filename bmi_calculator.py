# Building a BMI Calculator

# STEPS:
# 1. Ask user for weight in kg
# 2. Ask user for height in cm
# 3. Convert height to meters
# 4. Calculate BMI
# 5. Categorize BMI
# 6. Display result



# Code refactor - making code more modular

# Declared variables for weight and height for getting user inputs.
def get_user_input():
    """ 
        Declaring variables for weight and height for getting user inputs.
        Prompts the user to enter his/her weight and height.
        Returns:
        tuple: weight in kg (float), height in cm (float)
    """
    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))
    return weight, height_cm

# Converting height from cm to meters, then calculated bmi
def calculate_bmi(weight, height_cm):
    """
        Converting height from cm to meters.
        Then:
        Calculating the bmi using the WHO standards, 
        ready to be used for the conditional statements to
        determine the category a user fits in.
    
    """
    height_m = height_cm / 100
    # Calculating BMI
    bmi = weight / (height_m ** 2)
    return bmi

# Categorizing BMI using if-elif-else statements.
def categorize_bmi(bmi):
    """
    Categorizing BMI using if-elif-else statements.
    This allows users to know thier weight category according to the WHO bmi standards.

    Returns:
        str: The BMI category - Underweight, Normal weight, Overweight, or Obesity.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

# Displaying the result
def display_result(bmi, category):
    print(f"Your BMI is: {bmi:.2f}. You are classified as: {category}.")
    print("Thank you for using our BMI Calculator!")
    
# These function codes calculates the Body Mass Index (BMI) based on user input for weight and height.
# End of code - Works in the terminal



def main():
    weight, height_cm = get_user_input()
    bmi = calculate_bmi(weight, height_cm)
    category = categorize_bmi(bmi)
    result = display_result(bmi, category)

    return result



if __name__ == "__main__":
    main()
