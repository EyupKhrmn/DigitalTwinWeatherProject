# Ensure CORS is enabled in your Flask app to allow cross-origin requests
from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/weather')
def get_weather():
    db_conn = sqlite3.connect('../Databases/weatherAnkara.db')
    cursor = db_conn.cursor()
    cursor.execute("SELECT data FROM weather ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    db_conn.close()
    if row:
        return jsonify(json.loads(row[0]))
    else:
        return jsonify({"error": "No weather data found"}), 404

if __name__ == '__main__':
    app.run(port=5003,debug=True)