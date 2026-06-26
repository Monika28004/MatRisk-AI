class DualDomainArchitecture:

    def __init__(self):

        self.material_domain = [
            "Crystal Structure Encoding",
            "Property Prediction",
            "Failure Modelling",
            "Degradation Analysis"
        ]

        self.finance_domain = [
            "Commodity Trading",
            "Infrastructure Finance",
            "Insurance Pricing",
            "ESG Analytics"
        ]

    def display_architecture(self):

        print("\n=== MATERIAL DOMAIN ===")

        for module in self.material_domain:
            print(f"- {module}")

        print("\n=== FINANCIAL DOMAIN ===")

        for module in self.finance_domain:
            print(f"- {module}")