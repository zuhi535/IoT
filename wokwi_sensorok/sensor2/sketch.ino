#include <WiFi.h>
#include <PubSubClient.h>

// --- WiFi beállítások ---
// Wokwi-ban a virtuális WiFi neve: "Wokwi-GUEST", nincs jelszó
const char* ssid     = "Wokwi-GUEST";
const char* password = "";

// --- MQTT broker ---
// Kezdésnek használjuk a publikus test.mosquitto.org brokert
// (csak normál forgalomra, NEM támadásra!)
// Később átírjuk a SAJÁT brokered címére.
const char* mqtt_server = "test.mosquitto.org";
const int   mqtt_port   = 1883;

// Globális kliensek
WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastMsg = 0;

void setupWifi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("WiFi connected, IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Client ID legyen egyedi
    String clientId = "esp32-sensor1-";
    clientId += String(random(0xffff), HEX);

    // Nincs user/pass egyelőre
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Ha akarnál subscribe-olni, itt tennéd meg.
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  randomSeed(analogRead(0));  // véletlenszám a hőmérséklethez

  setupWifi();

  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastMsg > 5000) { // 5 másodpercenként küldünk egy mérést
    lastMsg = now;

    int temperature = random(20, 30); // 20–29°C közötti random érték

    char payload[128];
    snprintf(payload, sizeof(payload),
             "{\"sensor_id\":\"sensor1\",\"ts_device\":%lu,\"temperature\":%d}",
             now, temperature);

    const char* topic = "iot/lab/sensor1/temperature";

    Serial.print("Publishing to ");
    Serial.print(topic);
    Serial.print(": ");
    Serial.println(payload);

    client.publish(topic, payload);
  }
}
