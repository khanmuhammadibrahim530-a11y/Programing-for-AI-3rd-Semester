import student_utils


def parse_marks(text):
    """Convert comma-separated text into a validated list of marks."""

    if not text.strip():
        raise ValueError("Enter at least one mark.")

    parts = text.split(",")
    marks = []

    for part in parts:
        if not part.strip():
            raise ValueError("A mark is missing between commas.")

        mark = float(part.strip())

        if mark < 0 or mark > 100:
            raise ValueError("Every mark must be between 0 and 100.")

        marks.append(mark)

    return marks


def generate_summary(name, marks):
    """Generate a multi-line student report."""

    average = student_utils.calculate_average(marks)
    grade = student_utils.calculate_grade(average)

    report = f"""Student Name: {name}
Marks: {marks}
Average: {average:.2f}
Grade: {grade}"""

    return report


def save_report(filename, report):
    """Write the report to a UTF-8 text file."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
