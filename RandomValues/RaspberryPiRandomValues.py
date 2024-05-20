import random

def generate_rpi4_data():
    data = {
        "cpu_temperature": round(random.uniform(35.0, 85.0), 2),
        "cpu_usage": round(random.uniform(0, 100), 2),
        "ram_usage": round(random.uniform(0, 100), 2),
        "disk_usage": round(random.uniform(0, 100), 2),
        "power_usage": round(random.uniform(2.5, 7.5), 2),
        "energy_consumption": round(random.uniform(2.5, 7.5) * 24 / 1000, 4),
        "network_speed": random.randint(10, 1000),
        "gpu_temperature": round(random.uniform(30.0, 85.0), 2),
        "number_of_processes": random.randint(50, 200),
        "io_operations_per_second": random.randint(1000, 10000)
    }
    return data

rpi4_data = generate_rpi4_data()
print(rpi4_data)