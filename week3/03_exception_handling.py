try:
        age = int(input("Age: "))
        print("Age:", age)
except ValueError:
    print("Enter a whole number.")
try:
    numerator = float(input("Numerator: "))
    denominator = float(input("Denominator: "))
    result = numerator / denominator
except ValueError:
    print("Enter numeric values only.")
except ZeroDivisionError:
    print("The denominator cannot be zero.")
else:
    print("Result:", result)