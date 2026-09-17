def calculate_grade(marks):
  if marks >= 85:
    return "A"
  elif marks >= 70:
    return "B"
  elif marks >= 60:
    return "C"
  elif marks >= 50:
    return "D"
  else:
    return "F"


def calculate_bmi(weight_kg, height_m):
  bmi = weight_kg / (height_m**2)
  return bmi


# Lambda: returns the square of one number
square = lambda number: number**2


# *args collects all positional arguments into a tuple named marks
def calculate_average(*marks):
  return sum(marks) / len(marks)


# **kwargs collects all keyword arguments into a dictionary named details
def format_student(**details):
  # Fixed: Use single quotes for dictionary keys inside double-quoted f-string
  return f"{details['name']} studies {details['program']}"


def main():
  # Test the grade calculator
  print("Grade for 84:", calculate_grade(84))
  print("Grade for 85:", calculate_grade(85))
  print("Grade for 49:", calculate_grade(49))
  print("Grade for 50:", calculate_grade(50))

  # Test the BMI calculator
  print(f"BMI: {calculate_bmi(70, 1.75):.2f}")

  # Test the lambda function
  print("Square of 4:", square(4))

  # Test *args
  print("Average:", calculate_average(70, 80, 90))

  # Test **kwargs
  print(
      "Student:",
      format_student(name="Ali", program="AI"),
  )


# Run main() only when this file is executed directly,
# not when it is imported into another file.
if __name__ == "__main__":
  main()
