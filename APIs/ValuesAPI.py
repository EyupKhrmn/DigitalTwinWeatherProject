from flask import Flask, request, jsonify
from flask_cors import CORS
from TeachModel.Teach import predict_power_difference

app = Flask(__name__)
CORS(app)  # CORS politikalarını etkinleştir

@app.route('/predict', methods=['POST'])
def predict():
    # İstekten 'degree' değerlerini al ve bir liste olarak döndür
    degree_values = request.json.get('degree')

    # degree_values'ın bir liste olduğunu ve en az bir eleman içerdiğini kontrol et
    if not isinstance(degree_values, list) or len(degree_values) == 0:
        return jsonify({'error': 'degree_values must be a non-empty list'}), 400

    # Her bir derece değeri için güç farkını tahmin et ve bir listeye kaydet
    predicted_power_differences = []
    for degree in degree_values:
        predicted_power_difference = predict_power_difference([degree])

        # predicted_power_difference'ın bir liste olduğunu ve en az bir eleman içerdiğini kontrol et
        if not isinstance(predicted_power_difference, list) or len(predicted_power_difference) == 0:
            return jsonify({'error': 'predict_power_difference must return a non-empty list'}), 500

        predicted_power_differences.append(predicted_power_difference[0])

    # Tahminleri bir JSON yanıtı olarak döndür
    return jsonify({'predicted_power_differences': predicted_power_differences})

if __name__ == '__main__':
    app.run(port=5005)