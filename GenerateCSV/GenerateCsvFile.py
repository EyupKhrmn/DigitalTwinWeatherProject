import csv
import os
import random
from RandomValues.RaspberryPiRandomValues import generate_rpi4_data
from RandomValues.GetDayValue import GetDayValue
def generate_solar_panel_data():
    return {
        "Maximum Power (Pmax)": f"{random.uniform(230, 270)}W",
        "Voltage at Maximum Power (Vmp)": f"{random.uniform(28, 32)}V",
        "Current at Maximum Power (Imp)": f"{random.uniform(7.5, 9)}A",
        "Open-Circuit Voltage (Voc)": f"{random.uniform(36, 39)}V",
        "Short-Circuit Current (Isc)": f"{random.uniform(8.5, 9.1)}A",
        "Temperature Coefficient of Pmax": f"{random.uniform(-0.5, -0.3)}%/°C",
        "Nominal Operating Cell Temperature (NOCT)": f"{random.uniform(44, 46)}°C"
    }

def consolidate_data():
    rpi_data = generate_rpi4_data()
    solar_data = generate_solar_panel_data()
    weather_data = GetDayValue()
    consolidated_data = {**rpi_data, **solar_data, **weather_data}
    return consolidated_data

def save_data_to_csv(data, filename="consolidated_data.csv"):
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