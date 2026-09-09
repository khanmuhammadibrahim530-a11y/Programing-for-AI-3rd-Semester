weight=float(input("Enter weight kg: "))
height=float(input("Enter height in meters: "))
BMI = weight / (height ** 2)
print(BMI)
if  BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")
