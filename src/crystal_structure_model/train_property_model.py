from sklearn.ensemble import RandomForestRegressor
import joblib
import os

X = [
    [85, 7.8, 65],
    [60, 2.7, 90],
    [95, 4.5, 50],
    [75, 6.5, 70],
    [55, 2.5, 95]
]

y = [
    420,
    220,
    510,
    360,
    200
]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/crystal_model.pkl"
)

print("Model trained successfully.")