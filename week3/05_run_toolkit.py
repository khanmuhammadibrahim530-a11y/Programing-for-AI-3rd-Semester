import  student_toolkit


name = input("Enter student name: ")
marks_text = input("Enter marks separated by commas: ")

try:
   marks = student_toolkit.parse_marks(marks_text)
except ValueError as error:
   print("Invalid marks:", error)
else:
   report = student_toolkit.generate_summary(name, marks)
   print("\n" + report)
   student_toolkit.save_report("student_report.txt", report)
   print("\nReport saved as student_report.txt")