import student_utils

name = "Ayesha"
marks = [78, 86, 91]
average = student_utils.calculate_average(marks)
grade = student_utils.calculate_grade(average)
summary = student_utils.format_summary(name, average, grade)
print(summary)


name = "Abdullah"
marks = [88, 60, 81]
average = student_utils.calculate_average(marks)
grade = student_utils.calculate_grade(average)
summary = student_utils.format_summary(name, average, grade)
print(summary)