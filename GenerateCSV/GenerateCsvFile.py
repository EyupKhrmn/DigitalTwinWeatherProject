import csv
import os
import random
from RandomValues.GetDayValue import GetDayValue
def generate_solar_panel_data():
    return {
        "Current at Maximum Power (Imp)": f"{random.uniform(4.5, 6.6)}",
    }

def generate_rpi4_data():
    data = {
        "power_usage": round(random.uniform(2.5, 7.5), 2),
        "energy_consumption": round(random.uniform(2.5, 7.5) * 24 / 1000, 4),
    }
    return data
def consolidate_data():
    rpi_data = generate_rpi4_data()
    solar_data = generate_solar_panel_data()
    weather_data = GetDayValue()
    consolidated_data = {**rpi_data, **solar_data, **weather_data}
    return consolidated_data

def save_data_to_csv(data, filename="Required_data.csv"):
    file_exists = os.path.exists(filename)
    mode = 'a' if file_exists else 'w'
    header = not file_exists

    with open(filename, mode=mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if header:
            writer.writeheader()
        writer.writerow(data)

data_record = consolidate_data()
save_data_to_csv(data_record)