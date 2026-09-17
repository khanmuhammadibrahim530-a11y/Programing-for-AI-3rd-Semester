def average(a, b):
    return (a + b) / 2


print(f"G1 Corrected Output: {average(10, 20)}")


def double(number):
    return number * 2


result_g2 = double(5)
print(f"G2 Corrected Output: {result_g2}")


try:
    age = int(input("Age: "))
except ValueError:
    print("Error: Please enter a valid numeric value for age.")


def calculate_individual_grade(name, mark):
    if mark >= 85:
        print(f"{name}: A")
    elif mark >= 70:
        print(f"{name}: B")
    else:
        print(f"{name}: below B")


calculate_individual_grade("Ali", 88)
calculate_individual_grade("Sara", 73)
calculate_individual_grade("Hamza", 62)
