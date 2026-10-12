def read_float(prompt, minimum, maximum):
    """Read and return a valid floating-point value within a range."""
    while True:
        raw_value = input(prompt)
        try:
            value = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if value < minimum or value > maximum:
            print(f"Value must be between {minimum} and {maximum}. Try again.")
            continue

        return value


def read_int(prompt, minimum):
    """Read and return a valid integer value that is at least minimum."""
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value < minimum:
            print(f"Value must be {minimum} or greater. Try again.")
            continue

        return value


def classify_support(attendance, assignment_average, missed_submissions):
    """Return the student support-priority category.

    Rules are applied in order; the first matching rule wins.
    """
    if attendance < 60 or missed_submissions >= 4:
        return "High priority"

    if attendance < 75 or assignment_average < 60 or missed_submissions >= 2:
        return "Moderate priority"

    return "Routine monitoring"


def format_message(category):
    """Return the advisory message associated with a support category."""
    messages = {
        "High priority": "Immediate academic support is recommended.",
        "Moderate priority": "Monitor progress and provide targeted guidance.",
        "Routine monitoring": "Continue routine monitoring.",
    }
    return messages[category]


def main():
    """Run the student support rule engine."""
    attendance = read_float("Attendance percentage: ", 0, 100)
    assignment_average = read_float("Assignment average: ", 0, 100)
    missed_submissions = read_int("Missed submissions: ", 0)

    category = classify_support(attendance, assignment_average, missed_submissions)
    advisory = format_message(category)

    print(f"\nSupport category: {category}")
    print(f"Advisory: {advisory}")


if __name__ == "__main__":
    main()
