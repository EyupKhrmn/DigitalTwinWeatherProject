import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Veri setini oku
df = pd.read_csv('/Users/eyupkahraman/Desktop/DigitalTwinWeatherProject/GenerateCSV/Required_data.csv')

# 'Current At Maximum Power' ve 'power_usage' değerlerinin farkını hesapla
df['power_difference'] = df['Current at Maximum Power (Imp)'].astype(float) - df['power_usage'].astype(float)

# Giriş (X) ve çıktı (y) değerlerini belirle
X = df[['degree']].astype(float)
y = df['power_difference']

# Veri setini eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lineer regresyon modelini oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yap
predictions = model.predict(X_test)


def predict_power_difference(degree_value):
    # degree_value'yu bir numpy array'e dönüştür
    degree_value = np.array([degree_value]).reshape(-1, 1)

    predicted_power_difference = model.predict(degree_value)

    # Tahmin edilen güç farkını tek bir değer olarak döndür
    return predicted_power_difference.tolist()
