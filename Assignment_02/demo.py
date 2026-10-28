'''DEMOO FILE: demo.py'''
from pathlib import Path

import pandas as pd

from patient_dataset import PatientDataset


def main():
    """Load, audit, clean, and save the supplied patient dataset."""
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "patients_messy.csv"
    output_dir = base_dir / "output"

    try:
        dataset = PatientDataset(csv_path)
        audit = dataset.audit()

        print("Patient Dataset Audit")
        print(f"Original rows: {audit['row_count']}")
        print(f"Exact duplicates to remove: {audit['exact_duplicate_count']}")
        print(f"Invalid age values: {audit['invalid_value_counts']['age']}")
        print(f"Invalid heart-rate values: {audit['invalid_value_counts']['heart_rate']}")

        cleaned = dataset.cleaned()
        print("Cleaning completed")
        print(f"Cleaned rows: {len(cleaned)}")
        print(f"Age values imputed: {int(cleaned['age_imputed'].sum())}")
        print(f"Heart-rate values imputed: {int(cleaned['heart_rate_imputed'].sum())}")
        print(cleaned.head())

        dataset.save_audit(output_dir / "audit.json")
        output_dir.mkdir(parents=True, exist_ok=True)
        cleaned.to_csv(output_dir / "patients_clean.csv", index=False)
        print("Saved: output/audit.json")
        print("Saved: output/patients_clean.csv")

    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_path}")
    except pd.errors.EmptyDataError:
        print("Error: the CSV file is empty.")
    except pd.errors.ParserError as error:
        print(f"Error: the CSV file could not be parsed: {error}")
    except ValueError as error:
        print(f"Data problem: {error}")
    except OSError as error:
        print(f"File system problem: {error}")


if __name__ == "__main__":
    main()