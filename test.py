import joblib

model = joblib.load("models/gesture_svm.pkl")
print("MODEL OK")

scaler = joblib.load("models/scaler.pkl")
print("SCALER OK")