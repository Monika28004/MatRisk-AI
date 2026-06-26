class InfrastructureFinance:

    def estimate_loss(
        self,
        project_value,
        failure_probability
    ):

        return round(
            project_value * failure_probability,
            2
        )