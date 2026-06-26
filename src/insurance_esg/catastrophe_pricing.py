class CatastrophePricing:

    def calculate_premium(
        self,
        asset_value,
        failure_probability
    ):

        base_rate = 0.02

        premium = (
            asset_value *
            base_rate *
            (1 + failure_probability)
        )

        return round(premium, 2)