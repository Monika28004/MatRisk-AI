class PortfolioAnalytics:

    def evaluate(
        self,
        esg_score
    ):

        if esg_score >= 80:
            return "Excellent"

        elif esg_score >= 60:
            return "Good"

        elif esg_score >= 40:
            return "Moderate"

        return "Poor"