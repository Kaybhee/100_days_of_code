height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))
BMI_INDEX = weight / height** 2
if BMI_INDEX < 18.5:
    print(f"Your BMI index is {BMI_INDEX}, You are underweight")
elif BMI_INDEX < 25:
    print(f"Your BMI index is {BMI_INDEX}, You have a normal weight")
elif BMI_INDEX < 30:
    print(f"Your BMI index is {BMI_INDEX}, You are overweight")
elif BMI_INDEX < 35:
    print(f"Your BMI index is {BMI_INDEX}, You are Obese")
else:
    print(f"Your BMI index is {BMI_INDEX}, You are clinically Obese")