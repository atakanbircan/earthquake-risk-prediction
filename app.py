from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# FastAPI uygulamasını başlat
app = FastAPI(title="Deprem Risk Tahmin API", version="1.0")

# Eğitilmiş modeli yükle
MODEL_PATH = "models/risk_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    model = None


# Kullanıcıdan gelecek veri formatını (şemasını) tanımla
class LocationData(BaseModel):
    latitude: float
    longitude: float
    depth: float


@app.get("/")
def home():
    return {"message": "Deprem Risk API'sine Hoş Geldiniz!"}


@app.post("/predict_risk")
def predict_risk(data: LocationData):
    if not model:
        return {"error": "Model bulunamadı, önce modeli eğitin."}

    # Modelin beklediği formata getir
    features = [[data.latitude, data.longitude, data.depth]]

    # Tahmin yap
    prediction = model.predict(features)[0]

    # Sonucu döndür
    return {
        "latitude": data.latitude,
        "longitude": data.longitude,
        "predicted_magnitude_risk": round(prediction, 2),
        "status": "High Risk" if prediction >= 5.0 else "Normal"
    }