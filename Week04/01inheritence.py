class Experiment:
    def __init__(self, experiment_id, model_name, dataset_name, accuracy):
        # Convert string accuracy to float if passed as string
        accuracy = float(accuracy)

        if accuracy < 0 or accuracy > 1:
            raise ValueError("Accuracy must be between 0 and 1.")

        self.experiment_id = str(experiment_id)
        self.model_name = str(model_name)
        self.dataset_name = str(dataset_name)
        self.accuracy = accuracy

    def to_dictionary(self):
        """Return the experiment details as a dictionary for JSON conversion."""
        return {
            "experiment_id": self.experiment_id,
            "model_name": self.model_name,
            "dataset_name": self.dataset_name,
            "accuracy": self.accuracy,
        }
""