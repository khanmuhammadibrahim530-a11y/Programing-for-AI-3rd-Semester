# Assignment 1 – Student Support Rule Engine

A command-line Python program that collects a student's attendance
percentage, assignment average, and number of missed submissions,
validates the input, applies a transparent set of rules, and displays
a support-priority category with an advisory message. This is a
rule-based program, not a machine-learning model.

## Support-Priority Rules

Rules are checked in order; the first matching rule determines the
category.

1. **High priority** – attendance < 60 OR missed submissions >= 4
2. **Moderate priority** – attendance < 75 OR assignment average < 60
   OR missed submissions >= 2
3. **Routine monitoring** – none of the above conditions are true

## Files

- **support_engine.py** – Contains `read_float()` and `read_int()` for
  validated input, `classify_support()` for rule-based classification,
  `format_message()` for advisory text, and `main()` to run the
  program end to end.
- **test_support_engine.py** – Contains assertion-based tests that
  check normal and boundary cases for `classify_support()` and
  `format_message()`.
- **README.md** – This file.

## Run Commands

From the repository root: