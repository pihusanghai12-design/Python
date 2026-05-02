height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))

BMI= weight/(height/100)**2

print("Your BMI is: ", BMI)
if BMI <=18.4:
    print("Underweight")
elif BMI <=24.9:
    print("Healthy") 
elif BMI <=29.9:
    print("Overweight") 
elif BMI <=34.9:
    print("Severely overweight") 
elif BMI <=39.9:
    print("Obese")
else:
    print("Severly Obese")                    