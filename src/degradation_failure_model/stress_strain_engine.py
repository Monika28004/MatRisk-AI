class StressStrainEngine:

    def utilization_ratio(
        self,
        strength,
        applied_stress
    ):

        return round(
            applied_stress / strength,
            2
        )