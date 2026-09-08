weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))

bmi = weight / height ** 2

print("BMI:", round(bmi, 2))