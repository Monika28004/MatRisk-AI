class RiskQuantification:

    def classify(
        self,
        probability
    ):

        if probability < 0.3:
            return "LOW"

        elif probability < 0.7:
            return "MEDIUM"

        return "HIGH"