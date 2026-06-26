class CapexRisk:

    def calculate(
        self,
        project_value,
        failure_probability
    ):

        return round(
            project_value *
            failure_probability *
            0.20,
            2
        )