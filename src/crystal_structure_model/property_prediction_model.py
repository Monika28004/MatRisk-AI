import joblib

class PropertyPredictionModel:

    def __init__(self):
        self.model = joblib.load("models/crystal_model.pkl")

    def predict_strength(self, features):

        prediction = self.model.predict([features])

        return round(prediction[0], 2)