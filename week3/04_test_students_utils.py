"""
Test script for student_utils functions.
Verifies normal and boundary cases using assertions.
"""

from student_utils import calculate_average, calculate_grade


def test_student_utilities():
    print("Running utility tests...")

    # 1. Normal Case: Standard marks list
    marks_normal = [78, 65, 92]
    avg_normal = calculate_average(marks_normal)  # 235 / 3 = 78.333...
    assert abs(avg_normal - 78.33) < 0.01, "Failed: Normal average calculation"
    assert calculate_grade(avg_normal) == "B", "Failed: Normal grade assignment"

    # 2. Boundary Case: Minimum passing mark for Grade D
    assert calculate_grade(50.0) == "D", "Failed: Boundary case 50.0 should be D"

    # 3. Boundary Case: Grade A maximum boundary and exact edge
    assert calculate_grade(85.0) == "A", "Failed: Boundary case 85.0 should be A"
    assert calculate_grade(100.0) == "A", "Failed: Boundary case 100.0 should be A"

    # 4. Edge Case: Empty list handling
    assert calculate_average([]) == 0.0, "Failed: Empty list should return 0.0 average"

    # 5. Boundary Case: Failing grade exact boundary
    assert calculate_grade(49.9) == "F", "Failed: Boundary case 49.9 should be F"

    print("All 5+ assertions passed successfully! 🎉")


if __name__ == "__main__":
    test_student_utilities()
