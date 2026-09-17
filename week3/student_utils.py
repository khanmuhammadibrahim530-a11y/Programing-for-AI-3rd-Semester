def calculate_grade(marks):
    """Return A, B, C, D, or F using the stated boundaries.

    Args:
        marks: Numeric mark value to evaluate.

    Returns:
        The corresponding letter grade as a string.
    """
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


def calculate_average(marks):
    """Return the arithmetic mean of a non-empty list.

    Args:
        marks: A list of numeric marks.

    Returns:
        The arithmetic mean of the supplied marks, or 0.0 if empty.
    """
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def format_summary(name, average, grade):
    """Return one formatted summary string; do not print inside the function.

    Args:
        name: Name of the student.
        average: Calculated average mark.
        grade: Letter grade letter.

    Returns:
        A formatted summary string containing student details.
    """
    return f"Student: {name} | Average: {average:.2f} | Grade: {grade}"
