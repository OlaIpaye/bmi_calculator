# Building a BMI Calculator

# STEPS:
# 1. Ask user for weight in kg
# 2. Ask user for height in cm
# 3. Convert height to meters
# 4. Calculate BMI
# 5. Categorize BMI
# 6. Display result







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
print("Thank you for using our BMI Calculator!")

# This code calculates the Body Mass Index (BMI) based on user input for weight and height.
# End of code - Works in the terminal


# Code refactor - making code more modular
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


def main():
    weight, height_cm = get_user_input()



    pass



if __name__ == "__main__":
    main()


