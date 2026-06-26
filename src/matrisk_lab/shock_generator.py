import random

class ShockGenerator:

    def generate(self):

        events = [
            "Bridge Failure",
            "Steel Supply Shock",
            "Commodity Price Surge",
            "Insurance Catastrophe",
            "ESG Downgrade"
        ]

        return random.choice(events)