obtained_marks = float(input("Enter obtained marks: "))
total_marks = float(input("Enter total possible marks: "))

percentage = (obtained_marks / total_marks) * 100

print("Percentage:", round(percentage, 2))