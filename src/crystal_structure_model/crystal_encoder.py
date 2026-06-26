class CrystalEncoder:

    def encode(self, material):

        materials = {
            "Steel Alloy A": {
                "hardness": 85,
                "density": 7.8,
                "conductivity": 65
            },

            "Aluminum Alloy B": {
                "hardness": 60,
                "density": 2.7,
                "conductivity": 90
            },

            "Titanium Alloy C": {
                "hardness": 95,
                "density": 4.5,
                "conductivity": 50
            }
        }

        return materials.get(material)