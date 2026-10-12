import json
from pathlib import Path
from experiment import Experiment

# Setup relative paths
lab_folder = Path(__file__).resolve().parent
json_path = lab_folder / "data" / "experiments.json"
report_path = lab_folder / "reports" / "experiment_summary.txt"


def add_experiment(experiments, experiment_id, model_name, dataset_name, accuracy):
    """Create, validate, and add an experiment."""
    try:
        acc_float = float(accuracy)
    except (ValueError, TypeError):
        raise ValueError("Accuracy must be a valid number.")

    experiment = Experiment(experiment_id, model_name, dataset_name, acc_float)
    experiments.append(experiment)
    return experiment


def display_experiments(experiments):
    """Display the details of all experiments."""
    if not experiments:
        print("No experiments are available")
        return

    for exp in experiments:
        print(f"{exp.experiment_id} | {exp.model_name} | {exp.dataset_name} | Accuracy: {exp.accuracy}")


def search_experiment(experiments, experiment_id):
    """Search for an experiment by ID. Returns matching Experiment or None."""
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
    """Save all experiments as a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    experiment_records = [exp.to_dictionary() for exp in experiments]

    with path.open("w", encoding="utf-8") as file:
        json.dump(experiment_records, file, indent=4)


def load_experiments(file_path):
    """Load experiments from a JSON file."""
    path = Path(file_path)
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return [
                Experiment(d["experiment_id"], d["model_name"], d["dataset_name"], d["accuracy"])
                for d in data
            ]
    except json.JSONDecodeError:
        print("Error: Invalid JSON data format in file.")
        return []


def write_summary(experiments, file_path):
    """Write experiment summary to a text report."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = ["=== AI Experiment Tracker Summary ===\n\n", "All Experiments:\n"]
    for exp in experiments:
        lines.append(f"- {exp.experiment_id} | {exp.model_name} | Accuracy: {exp.accuracy}\n")

    best = find_best_experiment(experiments)
    if best:
        lines.append(f"\nBest Experiment:\n{best.experiment_id} | {best.model_name} | Accuracy: {best.accuracy}\n")

    with path.open("w", encoding="utf-8") as file:
        file.writelines(lines)


def run_assertions():
    """Run required lab tests."""
    exp1 = Experiment("EXP-TEST", "Model", "Data", "0.85")
    assert exp1.accuracy == 0.85

    d = exp1.to_dictionary()
    assert d["experiment_id"] == "EXP-TEST" and d["accuracy"] == 0.85

    test_list = [exp1]
    assert search_experiment(test_list, "EXP-TEST") is exp1
    assert search_experiment(test_list, "UNKNOWN") is None

    exp2 = Experiment("EXP-TEST-2", "Model2", "Data2", 0.95)
    test_list.append(exp2)
    assert find_best_experiment(test_list) is exp2

    try:
        Experiment("FAIL", "Model", "Data", 1.5)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def main():
    run_assertions()
    print("Assertions passed successfully!")

    experiments = load_experiments(json_path)
    print(f"Loaded {len(experiments)} records at startup.")

    if not experiments:
        add_experiment(experiments, "EXP-001", "Logistic Regression", "Student Performance", 0.84)
        add_experiment(experiments, "EXP-002", "Decision Tree", "Student Performance", 0.88)
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
        print(f"Best Model: {best.model_name} with Accuracy: {best.accuracy}")

    save_experiments(experiments, json_path)
    write_summary(experiments, report_path)

    reloaded = load_experiments(json_path)
    print(f"\nReloaded {len(reloaded)} records successfully.")
    assert len(reloaded) == len(experiments), "Reload count mismatch!"


if __name__ == "__main__":
    main()