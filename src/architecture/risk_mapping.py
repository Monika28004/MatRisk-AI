class RiskMapper:

    def map_material_to_finance(self):

        mapping = {

            "Material Failure":
                "Infrastructure Loss",

            "Material Degradation":
                "Maintenance Cost Increase",

            "Supply Material Shortage":
                "Commodity Price Spike",

            "Catastrophic Failure":
                "Insurance Claim Event",

            "Low Sustainability":
                "ESG Risk Increase"
        }

        return mapping