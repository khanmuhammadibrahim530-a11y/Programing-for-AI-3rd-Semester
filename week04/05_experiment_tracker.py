import json
from pathlib import Path
from experiment import Experiment

lab_folder = Path(__file__).resolve().parent
json_path = lab_folder / "data" / "experiments.json"
report_path = lab_folder / "reports" / "experiment_summary.txt"


def add_experiment(experiments, experiment_id, model_name, dataset_name, accuracy):
    """Create, validate, and add an experiment."""
    try:
        accuracy = float(accuracy)
    except (ValueError, TypeError):
        raise ValueError("Accuracy must be a valid numeric value.")

    experiment = Experiment(experiment_id, model_name, dataset_name, accuracy)
    experiments.append(experiment)
    return experiment


def display_experiments(experiments):
    """Display the details of all experiments."""
    if not experiments:
        print("No experiments are available")
        return

    for exp in experiments:
        print(
            f"{exp.experiment_id} | {exp.model_name} | {exp.dataset_name} | Accuracy: {exp.accuracy}"
        )


def search_experiment(experiments, experiment_id):
    """Search for an experiment by its ID."""
    for exp in experiments:
        if exp.experiment_id == experiment_id:
            return exp
    return None


def find_best_experiment(experiments):
    """Find and return the experiment with the highest accuracy."""
    if not experiments:
        return None
    return max(experiments, key=lambda exp: exp.accuracy)


def save_experiments(experiments, file_path):
    """Save experiments to a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    records = []
    for exp in experiments:
        records.append(exp.to_dictionary())

    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
    except PermissionError:
        print(f"Permission error: Cannot write to {path}")


def load_experiments(file_path):
    """Load experiments from a JSON file."""
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        loaded_experiments = []
        for d in data:
            exp = Experiment(
                d["experiment_id"], d["model_name"], d["dataset_name"], d["accuracy"]
            )
            loaded_experiments.append(exp)

        return loaded_experiments

    except json.JSONDecodeError:
        print("Error: JSON file data is invalid or corrupted.")
        return []


def write_summary(experiments, file_path):
    """Write an experiment summary report to a text file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    summary_lines = ["=== AI Experiment Tracker Summary ===\n\n", "All Experiments:\n"]

    for exp in experiments:
        summary_lines.append(
            f"- ID: {exp.experiment_id} | Model: {exp.model_name} | Accuracy: {exp.accuracy}\n"
        )

    best = find_best_experiment(experiments)
    if best:
        summary_lines.append(
            f"\nBest Experiment:\nID: {best.experiment_id} | Model: {best.model_name} | Accuracy: {best.accuracy}\n"
        )

    with path.open("w", encoding="utf-8") as file:
        file.writelines(summary_lines)


def run_assertions():
    """Run tests required for Part G."""
    # 1. Test string accuracy conversion to float
    exp1 = Experiment("EXP-TEST", "Model A", "Dataset A", "0.85")
    assert exp1.accuracy == 0.85

    # 2. Test object conversion to dictionary
    data_dict = exp1.to_dictionary()
    assert data_dict["experiment_id"] == "EXP-TEST" and data_dict["accuracy"] == 0.85

    # 3. Test successful search
    test_list = [exp1]
    assert search_experiment(test_list, "EXP-TEST") is exp1

    # 4. Test search for missing ID returns None
    assert search_experiment(test_list, "UNKNOWN") is None

    # 5. Test best experiment selection
    exp2 = Experiment("EXP-TEST2", "Model B", "Dataset B", 0.95)
    test_list.append(exp2)
    assert find_best_experiment(test_list) is exp2

    # 6. Test invalid accuracy raises ValueError
    try:
        Experiment("FAIL", "Model", "Dataset", 1.5)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def main():
    run_assertions()
    print("All assertions passed successfully!")

    experiments = load_experiments(json_path)
    print(f"Loaded {len(experiments)} records at startup.")

    if not experiments:
        add_experiment(
            experiments, "EXP-001", "Logistic Regression", "Student Performance", 0.84
        )
        add_experiment(
            experiments, "EXP-002", "Decision Tree", "Student Performance", 0.88
        )
        add_experiment(experiments, "EXP-003", "KNN", "Student Performance", 0.91)

    print("\n--- All Experiments ---")
    display_experiments(experiments)

    print("\n--- Search EXP-002 ---")
    found = search_experiment(experiments, "EXP-002")
    if found is not None:
        print(found.to_dictionary())
    else:
        print("Experiment was not found.")

    print("\n--- Best Experiment ---")
    best = find_best_experiment(experiments)
    if best:
        print(f"Model: {best.model_name} | Accuracy: {best.accuracy}")

    save_experiments(experiments, json_path)
    write_summary(experiments, report_path)

    reloaded_experiments = load_experiments(json_path)
    print(f"\nReloaded {len(reloaded_experiments)} records successfully.")
    assert len(reloaded_experiments) == len(experiments), (
        "Reloaded record count mismatch!"
    )


if __name__ == "__main__":
    main()
