import paho.mqtt.client as mqtt
import ssl
import csv
from datetime import datetime

BROKER = "localhost"
PORT = 8883
TOPIC = "iot/lab/#"

CSV_FILE = "measurements_tls.csv"

csv_file = open(CSV_FILE, mode="w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["recv_time", "topic", "payload"])


def on_connect(client, userdata, flags, rc):
    print("Connected to broker (TLS) with result code", rc)
    client.subscribe(TOPIC)
    print("Subscribed to", TOPIC)


def on_message(client, userdata, msg):
    recv_time = datetime.utcnow().isoformat()
    payload = msg.payload.decode("utf-8")
    print(f"[{recv_time}] Topic: {msg.topic} | Payload: {payload}")
    csv_writer.writerow([recv_time, msg.topic, payload])
    csv_file.flush()


client = mqtt.Client()

# !!! CALLBACKEK BEÁLLÍTÁSA !!!
client.on_connect = on_connect
client.on_message = on_message

# TLS beállítás - a ca.crt ugyanebben a mappában van
client.tls_set(
    ca_certs="ca.crt",
    certfile=None,
    keyfile=None,
    tls_version=ssl.PROTOCOL_TLS_CLIENT,
)

# ha nagyon szigorú lenne a cert-ellenőrzés, ideiglenesen bekapcsolható:
# client.tls_insecure_set(True)

client.connect(BROKER, PORT, 60)

print("Starting MQTT TLS collector...")
try:
    client.loop_forever()
finally:
    csv_file.close()
