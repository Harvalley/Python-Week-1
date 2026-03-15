# Week 1: A BMI Calculator

# User Info
weight = float(input("Enter your Weight: "))
height = float(input("Enter your Height: "))

# Calculate BMI
height_m = height / 100
bmi = weight / height * height

# Result
print("Your Weight is: ", round(bmi, 1))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")