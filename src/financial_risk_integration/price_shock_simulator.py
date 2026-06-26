class PriceShockSimulator:

    def simulate(
        self,
        base_price,
        risk_level
    ):

        if risk_level == "LOW":
            multiplier = 1.05

        elif risk_level == "MEDIUM":
            multiplier = 1.15

        else:
            multiplier = 1.30

        return round(
            base_price * multiplier,
            2
        )