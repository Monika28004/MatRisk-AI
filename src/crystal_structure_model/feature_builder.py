class FeatureBuilder:

    def build(self, material_data):

        return [
            material_data["hardness"],
            material_data["density"],
            material_data["conductivity"]
        ]