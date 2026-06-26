class ScenarioManager:

    def severity(self, event):

        mapping = {

            "Bridge Failure": 9,
            "Steel Supply Shock": 7,
            "Commodity Price Surge": 6,
            "Insurance Catastrophe": 10,
            "ESG Downgrade": 5
        }

        return mapping.get(event, 1)