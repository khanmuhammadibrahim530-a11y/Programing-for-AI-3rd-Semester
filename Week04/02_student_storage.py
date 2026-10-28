import csv
from pathlib import Path
from student import Student

def load_students(file_path):
    """Read student records from CSV and return a list of Student objects."""
    students = []
    csv_path = Path(file_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Missing file: {csv_path.name} in data directory.")

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks = [
                float(row["mark1"]),
                float(row["mark2"]),
                float(row["mark3"]),
            ]
            student = Student(row["sap_id"], row["name"], marks)
            students.append(student)

    return students


def save_student_report(student, file_path):
    """Create a formatted text report for an individual student."""
    report_path = Path(file_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    report_text = (
        f"SAP ID: {student.sap_id}\n"
        f"Student Name: {student.name}\n"
        f"Average Mark: {student.calculate_average():.2f}\n"
        f"Letter Grade: {student.calculate_grade()}\n"
    )

    try:
        with report_path.open("w", encoding="utf-8") as file:
            file.write(report_text)
    except PermissionError:
        print(f"Permission error: Unable to write report at {report_path}")


def main():
    lab_folder = Path(__file__).resolve().parent
    data_file = lab_folder / "data" / "students.csv"

    try:
        students = load_students(data_file)

        print("--- Loaded Students ---")
        total_class_marks = 0

        for student in students:
            print(student.format_profile())
            print()
            total_class_marks += student.calculate_average()

            # Save report file for each student
            report_file = lab_folder / "reports" / f"{student.sap_id}.txt"
            save_student_report(student, report_file)

        class_average = total_class_marks / len(students)
        print(f"Class Average: {class_average:.2f}")

        print("\n--- Saved Reports Check ---")
        for student in students:
            report_file = lab_folder / "reports" / f"{student.sap_id}.txt"
            print(f"Reading {report_file.name}:")
            print(report_file.read_text(encoding="utf-8"))

    except FileNotFoundError as error:
        print("File Error:", error)
    except ValueError as error:
        print("Data Error:", error)


if __name__ == "__main__":
    main()
