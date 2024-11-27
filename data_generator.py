import json
import random
import time
from datetime import datetime

# Load configuration
with open("config.json") as config_file:
    config = json.load(config_file)

# Generate random sensor data
def generate_sensor_data():
    return {
        "device_id": f"device_{random.randint(1, config['num_devices'])}",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(config['temperature_min'], config['temperature_max']), 2),
        "humidity": round(random.uniform(config['humidity_min'], config['humidity_max']), 2),
        "gps": {
            "lat": round(random.uniform(-90, 90), 6),
            "long": round(random.uniform(-180, 180), 6),
        },
    }

# Main loop to generate and send data
def main():
    print("Starting IoT Data Generator...")
    while True:
        data = generate_sensor_data()
        print(json.dumps(data))  # Print to console (can be sent to API or broker)
        time.sleep(config["frequency_seconds"])

if __name__ == "__main__":
    main()
