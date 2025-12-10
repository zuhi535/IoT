import paho.mqtt.client as mqtt
import json
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/lab/testsensor/temperature"

def main():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)

    for i in range(5):
        payload = {
            "sensor_id": "testsensor",
            "ts_device": int(time.time() * 1000),
            "temperature": 20 + i
        }
        payload_str = json.dumps(payload)

        print("Publishing:", payload_str)
        client.publish(TOPIC, payload_str)
        time.sleep(1)

    client.disconnect()
    print("Done.")

if __name__ == "__main__":
    main()
