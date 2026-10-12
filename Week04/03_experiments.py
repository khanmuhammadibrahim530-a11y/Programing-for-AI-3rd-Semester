import json
from pathlib import Path


class Experiment:
    def __init__(self, experiment_id, model_name, dataset_name, accuracy):
        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")
        self.experiment_id = experiment_id
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.accuracy = accuracy

    def to_dictionary(self):
        """Return the experiment details as a dictionary."""
        return {
            "experiment_id": self.experiment_id,
            "model_name": self.model_name,
            "dataset_name": self.dataset_name,
            "accuracy": self.accuracy,
        }


def save_experiments(experiments, file_path):
    """Save experiment objects into a JSON file."""
    json_path = Path(file_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    experiment_records = []
    for experiment in experiments:
        experiment_records.append(experiment.to_dictionary())

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(experiment_records, file, indent=4)


def load_experiments(file_path):
    """Load JSON records and convert them back to Experiment objects."""
    json_path = Path(file_path)

    with json_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    loaded_list = []
    for item in data:
        exp = Experiment(
            item["experiment_id"],
            item["model_name"],
            item["dataset_name"],
            item["accuracy"],
        )
        loaded_list.append(exp)

    return loaded_list


def main():
    lab_folder = Path(__file__).resolve().parent
    json_path = lab_folder / "data" / "experiments.json"

    experiments = [
        Experiment("EXP001", "Logistic regression", "student performance", 0.85),
        Experiment("EXP002", "Decision Tree", "Student performance", 0.78),
        Experiment("EXP003", "K-Nearest Neighbors", "student performance", 0.92),
    ]

    save_experiments(experiments, json_path)
    print("Experiments saved to:", json_path.resolve())

    # Load and display best experiment
    loaded_experiments = load_experiments(json_path)
    best_experiment = max(loaded_experiments, key=lambda exp: exp.accuracy)

    print("\nBest Experiment Loaded:")
    print("ID:", best_experiment.experiment_id)
    print("Model:", best_experiment.model_name)
    print("Accuracy:", best_experiment.accuracy)


if __name__ == "__main__":
    main()