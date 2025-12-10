import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/lab/sensor1/temperature"

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code", rc)
    client.subscribe(TOPIC)
    print("Subscribed to", TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"[MSG] Topic: {msg.topic} | Payload: {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Starting MQTT loop...")
client.loop_forever()
