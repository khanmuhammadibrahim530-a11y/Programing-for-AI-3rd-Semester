"""Assertion tests for PatientDataset."""

import json
import tempfile
from pathlib import Path

from patient_dataset import PatientDataset

BASE_DIR = Path(__file__).resolve().parent
SUPPLIED = BASE_DIR / "data" / "patients_messy.csv"


def write_csv(folder, name, text):
    """Write a temporary CSV file and return its path."""
    path = Path(folder) / name
    path.write_text(text, encoding="utf-8")
    return path


def main():
    """Run all tests."""
    dataset = PatientDataset(SUPPLIED)
    raw_before = dataset.raw.copy(deep=True)

    # 1. Missing required column
    try:
        dataset.validate_required(["patient_id", "blood_pressure"])
        raise AssertionError("ValueError was not raised")
    except ValueError:
        pass

    # 2. Original-data audit
    audit = dataset.audit()
    assert audit["row_count"] == 100
    assert audit["exact_duplicate_count"] == 1
    assert audit["invalid_value_counts"]["age"] == 4
    assert audit["invalid_value_counts"]["heart_rate"] == 2

    # 3. Duplicate removal
    cleaned = dataset.cleaned()
    assert len(cleaned) == 99

    # 4. Ranges after cleaning
    assert cleaned["age"].between(0, 120).all()
    assert cleaned["heart_rate"].between(30, 220).all()

    # 5. Medians and flags
    assert int(cleaned["age_imputed"].sum()) == 11
    assert int(cleaned["heart_rate_imputed"].sum()) == 9
    assert (cleaned.loc[cleaned["age_imputed"], "age"] == 52).all()
    assert (cleaned.loc[cleaned["heart_rate_imputed"], "heart_rate"] == 80.5).all()

    # 6. Conflicting repeated ID
    with tempfile.TemporaryDirectory() as folder:
        path = write_csv(
            folder,
            "conflict.csv",
            "patient_id,age,heart_rate,department\n"
            "P1,40,70,Cardio\n"
            "P1,41,70,Cardio\n",
        )
        try:
            PatientDataset(path).cleaned()
            raise AssertionError("ValueError was not raised")
        except ValueError:
            pass

    # 7. Original data preserved
    assert dataset.raw.equals(raw_before)

    # 8. Independent cleaned result
    cleaned.loc[0, "age"] = 999
    assert dataset.raw.equals(raw_before)

    # 9. Boundary values stay valid
    with tempfile.TemporaryDirectory() as folder:
        path = write_csv(
            folder,
            "boundary.csv",
            "patient_id,age,heart_rate,department\n"
            "A1,0,30,Cardio\n"
            "A2,120,220,Neurology\n"
            "A3,50,100,Orthopedics\n",
        )
        result = PatientDataset(path).cleaned()
        assert not result["age_imputed"].any()
        assert not result["heart_rate_imputed"].any()

    # 10. Saved audit is valid JSON
    with tempfile.TemporaryDirectory() as folder:
        json_path = Path(folder) / "audit.json"
        dataset.save_audit(json_path)
        with json_path.open(encoding="utf-8") as file:
            loaded = json.load(file)
        assert loaded["row_count"] == 100

    print("All tests passed.")


if __name__ == "__main__":
    main()