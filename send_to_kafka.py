from kafka import KafkaProducer
import json
import time
from data_generator.vehicle_data_simulator import generate_vehicle_data

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    message = generate_vehicle_data()
    producer.send('vehicle_data', value=message)
    print(f"Sent: {message}")
    time.sleep(1)
