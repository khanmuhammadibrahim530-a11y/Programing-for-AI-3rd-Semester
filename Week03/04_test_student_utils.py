import student_utils

assert student_utils.calculate_grade(85) == "A"
assert student_utils.calculate_grade(85) == "C"
assert student_utils.calculate_grade(85) == "D"
assert student_utils.calculate_grade(85) == "B"
assert student_utils.calculate_grade(49) == "F"
assert student_utils.calculate_average([60, 70, 80]) == 70
assert student_utils.calculate_average([50, 60]) == 55.0
print("All assertion checks passed.")