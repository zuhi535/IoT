# IoT security: támadási felületek azonosítása és védelmi mechanizmusok fejlesztése

**Alcím:** IoT eszközök sebezhetőségi elemzése, biztonságos hálózati protokollok alkalmazása

Ez a repó a BSc szakdolgozathoz tartozó anyagokat tartalmazza.  
A projekt célja egy MQTT-alapú IoT-rendszer **biztonsági vizsgálata és szimulált elemzése**, különös tekintettel a kommunikációs védelemre, a támadási szcenáriók modellezésére és a mérési eredmények kiértékelésére.

A projekt főbb elemei:

- MQTT alapú kommunikáció ESP32 szenzorok és broker között
- titkosítatlan és védett kommunikáció összehasonlítása
- támadási szcenáriók modellezése
- mérési eredmények gyűjtése és elemzése
- egyszerű MI-alapú anomáliadetektálási kísérlet

---
Wokwi_sersor_1: https://wokwi.com/projects/449908585893820417
Wokwi_sersor_2: https://wokwi.com/projects/449908624240245761
---
## Könyvtárstruktúra

```text
.
├── CSV/
│   ├── measurements.csv
│   ├── measurements_attack.csv
│   ├── measurements_attack_old.csv
│   ├── measurements_attack_only.csv
│   ├── measurements_normal.csv
│   ├── measurements_old.csv
│   └── measurements_tls_old.csv
│
├── kódok/
│   ├── analyze_measurements.py
│   ├── analyze_measurements_tls.py
│   ├── attack_publisher_tls.py
│   ├── ca.crt
│   ├── collector.py
│   ├── collector_tls.py
│   ├── create_mixed_attack_dataset.py
│   ├── ml_anomaly_detector.py
│   ├── pub_test.py
│   ├── pub_test_tls.py
│   ├── subscriber.py
│   └── tls_sensors.py
│
├── wokwi_sensorok/
│   ├── sensor_1/
│   │   ├── diagram.json
│   │   ├── libraries.txt
│   │   └── sketch.ino
│   └── sensor_2/
│       ├── diagram.json
│       ├── libraries.txt
│       └── sketch.ino
│
├── README.md
└── szakdolgozat_iot.pdf
