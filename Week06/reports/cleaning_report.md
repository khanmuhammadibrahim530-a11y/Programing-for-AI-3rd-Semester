# Week 6 Cleaning Report

**Name:** Muhammad Ibrahim
**SAP ID:** 72404
**Dataset:** students_messy.csv (synthetic practice data)

## 1. Overview
- Raw rows: 11 → Clean rows: 10 (1 exact duplicate removed).
- Raw data in `data/raw/` was not modified. All outputs are saved in `data/processed/` and `reports/`.

## 2. Cleaning decisions

### Duplicates
- Student 1003 appeared twice with identical values. I kept the first occurrence and removed the other.
- After removal, no student_id was repeated.

### Text standardization
- Program labels (`BS AI`, `BS-AI`, `AI`, `BS DS`) were mapped to `BSAI` or `BSDS` after stripping spaces and uppercasing. `BSCS` was kept as it is.
- Cities were title-cased, `Rwp` was replaced with `Rawalpindi`, and the missing city (student 1008) was filled with `Unknown`.

### Types and dates
- Assessment columns were converted with `pd.to_numeric(errors="coerce")`.
- ISO-style dates (e.g. 2025-09-01) were parsed year-first. Other formats were parsed with `dayfirst=True`.
- `09-01-2025` (student 1004) was parsed as 9 January 2025. This date is ambiguous and the intended date should be verified with the source.

### Invalid values (outside 0–100)
- Student 1004 attendance = 110 and student 1009 attendance = -5 were replaced with missing values and then imputed.
- Details are saved in `invalid_records.csv` and `cleaning_log.csv`.

### Missing values
- Attendance (1002, 1004, 1009): filled with the program median. If the program had no valid value, the overall median (81) was used.
- Assignment (1010) = 80, midterm (1003) = 72, final (1005) = 81: filled with column medians.
- Imputed values are marked in the `*_imputed` columns.

## 3. Results
- Program summary: BSAI 6 students (average 74.95), BSCS 2 (66.40), BSDS 2 (83.75).
- Grade distribution: A = 2, B = 5, C = 1, D = 1, F = 1.
- At-risk students: 1005, 1007, 1009.

## 4. Limitations
- Median imputation reduces variation and can change grades and risk labels. For example, the final mark of student 1005 (81) is an estimate and affects their grade.
- Attendance for 1004 and 1009 was filled with a median, so their attendance status is not based on real data.
- The weights (20/30/50) are exercise weights, not the official course policy.
- These are synthetic records. Official marks need source verification and authorization.