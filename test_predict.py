import joblib

model = joblib.load("model.pkl")

prediction = model.predict([[70]])

print("Predict", prediction)
