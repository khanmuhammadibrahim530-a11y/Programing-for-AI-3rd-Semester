import csv
import json
from pathlib import Path


# F1. Missing self
# Error: NameError / TypeError when accessing attributes.
# Cause: Constructor omitted 'self' in the parameter list.
# Fix: Added 'self' as the first parameter.
class CorrectedStudent:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


# F2. Wrong file mode
# Error: io.UnsupportedOperation: not writable
# Cause: File opened in read mode ("r") instead of write mode ("w").
# Fix: Changed mode from "r" to "w".
def fix_csv_writer():
    file_path = Path("week04/data/debug_students.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Ali", 85])


# F3. Raw object in JSON
# Error: TypeError: Object of type Model is not JSON serializable
# Cause: Attempting to dump a raw Python class instance into JSON.
# Fix: Converted the object using a custom dictionary helper function.
class DummyModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def to_dict(self):
        return {"model_name": self.model_name}


def fix_json_dump():
    model = DummyModel("CNN Model")
    file_path = Path("week04/data/debug_model.json")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(model.to_dict(), file, indent=4)


if __name__ == "__main__":
    # Test F1
    student = CorrectedStudent("Hamza", [80, 90])
    print("F1 Fix Result:", student.name, student.marks)

    # Test F2
    fix_csv_writer()
    print("F2 Fix Result: CSV file written in 'w' mode.")

    # Test F3
    fix_json_dump()
    print("F3 Fix Result: Custom object converted to dict and saved as JSON.")
