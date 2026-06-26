class ESGScoringEngine:

    def calculate(
        self,
        failure_probability
    ):

        score = 100 - (
            failure_probability * 100
        )

        return round(score, 2)