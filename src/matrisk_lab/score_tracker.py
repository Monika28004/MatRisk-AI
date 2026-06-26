class ScoreTracker:

    def calculate_score(
        self,
        severity
    ):

        return max(
            0,
            100 - (severity * 10)
        )