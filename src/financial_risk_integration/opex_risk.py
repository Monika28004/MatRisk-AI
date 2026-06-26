class OpexRisk:

    def calculate(
        self,
        project_value,
        failure_probability
    ):

        return round(
            project_value *
            failure_probability *
            0.10,
            2
        )