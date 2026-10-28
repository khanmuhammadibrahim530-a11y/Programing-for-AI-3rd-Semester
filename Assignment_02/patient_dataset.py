"""Patient dataset audit toolkit for Assignment 2."""

import json
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["patient_id", "age", "heart_rate", "department"]
MISSING_MARKERS = ["", "missing", "N/A", "-"]
NUMERIC_RANGES = {"age": (0, 120), "heart_rate": (30, 220)}
DEPARTMENT_MAP = {
    "GEN MED": "GENERAL MEDICINE",
    "GENERAL MED": "GENERAL MEDICINE",
    "GENERAL-MED": "GENERAL MEDICINE",
    "CARDIO": "CARDIOLOGY",
}


class PatientDataset:
    """Load, audit, and clean a synthetic patient dataset."""

    def __init__(self, path):
        """Load the CSV and retain the original DataFrame."""
        self.path = Path(path)
        self.raw = pd.read_csv(
            self.path,
            na_values=MISSING_MARKERS,
            dtype={"patient_id": "string"},
        )

    def validate_required(self, columns):
        """Raise ValueError if required columns are missing."""
        missing = [name for name in columns if name not in self.raw.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        return None

    def audit(self):
        """Return a JSON-safe audit of the original data."""
        self.validate_required(REQUIRED_COLUMNS)

        missing_counts = {
            str(name): int(count) for name, count in self.raw.isna().sum().items()
        }
        exact_duplicate_count = int(self.raw.duplicated().sum())

        deduplicated = self.raw.drop_duplicates()
        repeated_id_count = int(deduplicated["patient_id"].duplicated().sum())

        invalid_value_counts = {}
        nonnumeric_counts = {}
        for column, (low, high) in NUMERIC_RANGES.items():
            original = self.raw[column]
            numbers = pd.to_numeric(original, errors="coerce")
            nonnumeric_counts[column] = int((original.notna() & numbers.isna()).sum())
            invalid_value_counts[column] = int(
                ((numbers < low) | (numbers > high)).sum()
            )

        labels = sorted(str(x) for x in self.raw["department"].dropna().unique())

        return {
            "row_count": int(len(self.raw)),
            "column_count": int(self.raw.shape[1]),
            "missing_counts": missing_counts,
            "exact_duplicate_count": exact_duplicate_count,
            "repeated_id_count": repeated_id_count,
            "invalid_value_counts": invalid_value_counts,
            "nonnumeric_counts": nonnumeric_counts,
            "department_labels": labels,
        }

    def cleaned(self):
        """Return an independent cleaned DataFrame."""
        self.validate_required(REQUIRED_COLUMNS)

        df = self.raw.copy(deep=True)
        df = df.drop_duplicates().reset_index(drop=True)

        df["patient_id"] = df["patient_id"].str.strip()
        if df["patient_id"].isna().any() or df["patient_id"].eq("").any():
            raise ValueError("Missing or empty patient_id found.")
        if df["patient_id"].duplicated().any():
            repeated = df.loc[df["patient_id"].duplicated(), "patient_id"].tolist()
            raise ValueError(f"Repeated patient_id after deduplication: {repeated}")

        department = df["department"].astype("object").str.strip().str.upper()
        department = department.replace(DEPARTMENT_MAP)
        department = department.mask(department == "")
        df["department"] = department.fillna("Unknown")

        for column, (low, high) in NUMERIC_RANGES.items():
            numbers = pd.to_numeric(df[column], errors="coerce")
            numbers = numbers.where((numbers >= low) & (numbers <= high))
            df[f"{column}_imputed"] = numbers.isna()
            valid = numbers.dropna()
            if valid.empty:
                raise ValueError(f"No valid values to calculate median for {column}.")
            df[column] = numbers.fillna(valid.median())

        return df

    def save_audit(self, path):
        """Save the original-data audit as JSON."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        audit = self.audit()
        with path.open("w", encoding="utf-8") as file:
            json.dump(audit, file, indent=4)