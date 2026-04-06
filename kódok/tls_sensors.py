import time
import json
import ssl
import random

import paho.mqtt.client as mqtt

BROKER = "localhost"   # ugyanaz, mint a TLS-es Mosquitto configban
PORT   = 8883

TOPICS = {
    "sensor1": "iot/lab/sensor1/temperature",
    "sensor2": "iot/lab/sensor2/temperature",
}

def main():
    client = mqtt.Client()

    # TLS beállítás – a ca.crt ugyanaz, amit a mosquitto is használ
    client.tls_set(
        ca_certs="ca.crt",
        certfile=None,
        keyfile=None,
        tls_version=ssl.PROTOCOL_TLS_CLIENT,
    )

    print("Connecting to TLS broker...")
    client.connect(BROKER, PORT, 60)
    print("Connected, starting publish loop...")

    start_ts = time.time()

    # pl. 60 másodpercig küldjünk adatot
    DURATION_SEC = 300

    while True:
        now = time.time()
        if now - start_ts > DURATION_SEC:
            break

        ts_device = int((now - start_ts) * 1000)

        for sensor_id, topic in TOPICS.items():
            temperature = random.randint(20, 30)

            payload = {
                "sensor_id": sensor_id,
                "ts_device": ts_device,
                "temperature": temperature,
            }

            payload_str = json.dumps(payload)
            print(f"Publishing to {topic}: {payload_str}")
            client.publish(topic, payload_str)

        # itt tudod szabályozni a rátát
        time.sleep(5.0)  # kb. 1 üzenet / s / szenzor

    print("Done.")
    client.disconnect()


if __name__ == "__main__":
    main()
