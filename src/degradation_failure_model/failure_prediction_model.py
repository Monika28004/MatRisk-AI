class FailurePredictionModel:

    def predict(
        self,
        utilization_ratio
    ):

        if utilization_ratio < 0.5:
            return 0.10

        elif utilization_ratio < 0.8:
            return 0.35

        elif utilization_ratio < 1.0:
            return 0.70

        return 0.95