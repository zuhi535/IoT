import time
import json
import random
import ssl

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 8883
TOPIC = "iot/lab/sensor1/temperature"
CA_CERT = "ca.crt"


def main():
    client = mqtt.Client()

    client.tls_set(
        ca_certs=CA_CERT,
        certfile=None,
        keyfile=None,
        tls_version=ssl.PROTOCOL_TLS_CLIENT,
    )

    print("[ATTACK] Kapcsolódás a TLS brokerhez...")
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    try:
        while True:
            temp = random.randint(60, 90)

            payload = {
                "sensor_id": "attack",
                "ts_device": int(time.time() * 1000),
                "temperature": temp
            }

            msg = json.dumps(payload)
            print(f"[ATTACK] Publish: {msg}")
            client.publish(TOPIC, msg)

            time.sleep(3)

    except KeyboardInterrupt:
        print("\n[ATTACK] Leállítva.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()