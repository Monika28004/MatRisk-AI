class DegradationSimulator:

    def simulate(self, initial_strength, years):

        degradation_rate = 0.05

        strength_history = []

        current_strength = initial_strength

        for year in range(1, years + 1):

            current_strength *= (1 - degradation_rate)

            strength_history.append(
                round(current_strength, 2)
            )

        return strength_history