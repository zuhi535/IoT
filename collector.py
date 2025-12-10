import paho.mqtt.client as mqtt
import csv
from datetime import datetime

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/lab/#"   # minden labos topicra feliratkozunk

CSV_FILE = "measurements.csv"

# Megnyitjuk a CSV-t és kiírjuk a fejlécet, ha új fájl
csv_file = open(CSV_FILE, mode="w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["recv_time", "topic", "payload"])

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code", rc)
    client.subscribe(TOPIC)
    print("Subscribed to", TOPIC)

def on_message(client, userdata, msg):
    recv_time = datetime.utcnow().isoformat()
    payload = msg.payload.decode("utf-8")
    print(f"[{recv_time}] Topic: {msg.topic} | Payload: {payload}")

    # Logolás CSV-be
    csv_writer.writerow([recv_time, msg.topic, payload])
    csv_file.flush()  # hogy azonnal lemezre kerüljön

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Starting MQTT collector...")
try:
    client.loop_forever()
finally:
    csv_file.close()
