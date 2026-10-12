import os
import numpy as np

# Ensure target directories exist before saving
os.makedirs("Week05/data", exist_ok=True)
os.makedirs("Week05/output", exist_ok=True)

# ==============================================================================
# F1. Incompatible shapes
# ==============================================================================
# Error: ValueError: operands could not be broadcast together with shapes (3,4) (3,2)
# Cause: Element-wise addition requires identical dimensions or dimensions compatible
#        with NumPy broadcasting rules. Here, column dimensions 4 and 2 do not match and neither is 1.
# Fix: Match array dimensions by creating 'b' with shape (3, 4) to add matrices of the same shape.

a = np.ones((3, 4))
b = np.ones((3, 4))  # Fixed: changed shape from (3, 2) to (3, 4)
result_f1 = a + b
print("--- F1. Incompatible Shapes Fixed ---")
print(result_f1)


# ==============================================================================
# F2. Array Boolean logic
# ==============================================================================
# Error: ValueError: The truth value of an array with more than one element is ambiguous.
# Cause: Python's built-in 'and' operator evaluates truthiness on whole objects (truth value of whole array),
#        which is ambiguous for NumPy arrays.
# Fix: Use NumPy's bitwise element-wise operator '&' and enclose each condition in parentheses ().

values = np.array([10, 20, 30, 40])
# Fixed: replaced 'and' with '&' and wrapped conditions in parentheses
selected = values[(values > 15) & (values < 35)]
print("\n--- F2. Array Boolean Logic Fixed ---")
print(selected)


# ==============================================================================
# F3. Wrong axis
# ==============================================================================
# Error: Incorrect output dimension (calculates average per column instead of per row).
# Cause: axis=0 computes the mean down columns (vertically), yielding 3 subject averages for 2 students.
# Fix: Change axis=0 to axis=1 to calculate the mean across rows (horizontally) for each student.

scores = np.array([[70, 80, 90], [60, 75, 85]])
# Fixed: changed axis=0 to axis=1
student_averages = np.mean(scores, axis=1)
print("\n--- F3. Wrong Axis Fixed ---")
print(student_averages)


# ==============================================================================
# Save and Reload & Verification
# ==============================================================================

# Sample setup data
patient_data = np.array(
    [
        [101, 45, 38.5, 100, 92],
        [102, 23, 36.8, 75, 98],
        [103, 67, 39.1, 110, 89],
        [104, 54, 37.0, 80, 96],
        [105, 34, 38.0, 95, 93],
        [106, 72, 36.5, 70, 97],
    ],
    dtype=float,
)

clinical_features = patient_data[:, 1:]
col_min = clinical_features.min(axis=0)
col_max = clinical_features.max(axis=0)
normalized_features = (clinical_features - col_min) / (col_max - col_min)

# 1. Save and reload .npy format
np.save("Week05/data/patient_data.npy", patient_data)
loaded_npy = np.load("Week05/data/patient_data.npy")

# 2. Save and reload .csv format
np.savetxt(
    "Week05/output/normalized_features.csv",
    normalized_features,
    delimiter=",",
    fmt="%.4f",
)
loaded_csv = np.loadtxt("Week05/output/normalized_features.csv", delimiter=",")

# Verification tests
npy_equal = np.array_equal(patient_data, loaded_npy)
csv_close = np.allclose(normalized_features, loaded_csv, atol=1e-4)

print("\n--- File Round-Trip Verifications ---")
print(f".npy exact round-trip match (np.array_equal): {npy_equal}")
print(f".csv rounded round-trip match (np.allclose): {csv_close}")
