class InsuranceRiskModel:

    def classify(
        self,
        failure_probability
    ):

        if failure_probability < 0.30:
            return "LOW"

        elif failure_probability < 0.70:
            return "MEDIUM"

        return "HIGH"