import random

def generate_solar_panel_data():
    data = {
        "Maximum Power (Pmax)": f"{random.uniform(230, 270)}W",  # Range around 250W
        "Voltage at Maximum Power (Vmp)": f"{random.uniform(28, 32)}V",  # Range around 30V
        "Current at Maximum Power (Imp)": f"{random.uniform(7.5, 9)}A",  # Range around 8.3A
        "Open-Circuit Voltage (Voc)": f"{random.uniform(36, 39)}V",  # Range around 37.5V
        "Short-Circuit Current (Isc)": f"{random.uniform(8.5, 9.1)}A",  # Range around 8.8A
        "Temperature Coefficient of Pmax": f"{random.uniform(-0.5, -0.3)}%/°C",  # Range around -0.4%/°C
        "Nominal Operating Cell Temperature (NOCT)": f"{random.uniform(44, 46)}°C"  # Range around 45°C
    }
    return data

solar_panel_data = generate_solar_panel_data()
for parameter, value in solar_panel_data.items():
    print(f"{parameter}: {value}")