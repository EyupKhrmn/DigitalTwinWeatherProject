import http.client
import certifi
import ssl
import json
import sqlite3

context = ssl.create_default_context(cafile=certifi.where())

conn = http.client.HTTPSConnection("api.collectapi.com", context=context)

headers = {
    'content-type': "application/json",
    'authorization': "apikey 4ttyekL5JKEfakJkQdv05i:1wYsGb1x78craBhIxsRXVj"
}

conn.request("GET", "/weather/getWeather?data.lang=tr&data.city=Kars", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

weather_data = json.loads(data.decode("utf-8"))


db_conn = sqlite3.connect('../Databases/weatherKars.db')

cursor = db_conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY,
        data TEXT
    )
''')

cursor.execute('''
    INSERT INTO weather (data) VALUES (?)
''', (json.dumps(weather_data),))

db_conn.commit()

db_conn.close()