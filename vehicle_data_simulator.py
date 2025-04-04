import random
import time
import json

VEHICLE_IDS = ['V001', 'V002', 'V003']

def generate_vehicle_data():
    return {
        "vehicle_id": random.choice(VEHICLE_IDS),
        "speed": round(random.uniform(0, 120), 2),
        "fuel_level": round(random.uniform(5, 100), 2),
        "engine_temp": round(random.uniform(70, 120), 2),
        "timestamp": time.time()
    }

while True:
    data = generate_vehicle_data()
    print(json.dumps(data))
    time.sleep(1)
