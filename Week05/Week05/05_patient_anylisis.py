import numpy as np

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

shape = patient_data.shape
print("Shape of the patient data:", shape)
patient_id = patient_data[:, 0]
print("patient ids are: ", patient_id)
clinical_features = patient_data[:, 1:]
print("Clinical features of the patients:\n", clinical_features)
age = clinical_features[:, 0]
print("Ages of the patients:\n", age)
avg = np.mean(age)
print("Average age of the patients:", avg)
means = np.mean(clinical_features, axis=0)
print("Mean values of clinical features:\n", means)
older = clinical_features
condition = (
    (patient_data[:, 1] > 60) & (patient_data[:, 2] > 38.0) & (patient_data[:, 4] < 94)
)
print(
    "Patients older than 60 with fever and low oxygen saturation:\n",
    patient_data[condition],
)
# 2. Find column-wise Min and Max (axis=0)
col_min = clinical_features.min(axis=0)
col_max = clinical_features.max(axis=0)

# 3. Apply Min-Max Formula: (X - min) / (max - min)
normalized_features = (clinical_features - col_min) / (col_max - col_min)

print("Min values per column:", col_min)
print("Max values per column:", col_max)
print("\nNormalized Clinical Features Matrix:")
print(np.round(normalized_features, 4))
