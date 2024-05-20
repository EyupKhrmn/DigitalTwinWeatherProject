import sqlite3
import json

'''
def GetDayValue():
    db_conn = sqlite3.connect('weatherTrabzon.db')
    cursor = db_conn.cursor()

    query = """
    SELECT data
    FROM weather
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)
    row = cursor.fetchone()

    if row:
        weather_data = json.loads(row[0])
        # Assuming the weather data contains a 'result' key with relevant weather information
        if 'result' in weather_data and weather_data['result']:
            latest_weather = weather_data['result'][0]  # Assuming the first item is the latest weather data
            return {
                "day": latest_weather.get('day', ''),
                "description": latest_weather.get('description', ''),
                "degree": latest_weather.get('degree', '')
            }
    db_conn.close()
    return {}
'''

import sqlite3
import json

def initialize_db():
    db_conn = sqlite3.connect('/Users/eyupkahraman/Desktop/DigitalTwinWeatherProject/Databases/weatherTrabzon.db')
    cursor = db_conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            data TEXT NOT NULL
        );
    ''')
    db_conn.commit()
    db_conn.close()

def GetDayValue():
    initialize_db()  # Veritabanı ve tablo kontrolü
    db_conn = sqlite3.connect('/Users/eyupkahraman/Desktop/DigitalTwinWeatherProject/Databases/weatherTrabzon.db')
    cursor = db_conn.cursor()

    query = """
    SELECT data
    FROM weather
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)
    row = cursor.fetchone()

    if row:
        weather_data = json.loads(row[0])
        if 'result' in weather_data and weather_data['result']:
            latest_weather = weather_data['result'][0]
            return {
                "day": latest_weather.get('day', ''),
                "description": latest_weather.get('description', ''),
                "degree": latest_weather.get('degree', '')
            }
    db_conn.close()
    return {}