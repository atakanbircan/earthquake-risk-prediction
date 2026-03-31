from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from data_loader import load_and_preprocess_data


def train_model(data_path: str, model_save_path: str):
    # 1. Veriyi getir
    X, y = load_and_preprocess_data(data_path)

    # 2. Train / Test olarak ayır (%80 eğitim, %20 test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Modeli Tanımla ve Eğit (Random Forest Regressor)
    print("Model eğitiliyor...")
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    # 4. Başarıyı Ölç
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Başarısı (Hata Oranı - MSE): {mse:.4f}")

    # 5. Modeli Kaydet (Backend'de kullanmak için)
    joblib.dump(model, model_save_path)
    print(f"Model başarıyla {model_save_path} konumuna kaydedildi.")


import os

if __name__ == "__main__":
    # Bu kod dosyanın nerede olduğunu bulup her zaman doğru yolu hesaplar
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, "..", "data", "earthquake_data.csv")
    model_file = os.path.join(current_dir, "..", "models", "risk_model.pkl")

    train_model(data_file, model_file)