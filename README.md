
# IoT security: támadási felületek azonosítása és védelmi mechanizmusok fejlesztése

**Alcím:** IoT eszközök sebezhetőségi elemzése, biztonságos hálózati protokollok alkalmazása

Ez a repó a BSc szakdolgozathoz tartozó anyagokat tartalmazza.  
A projekt célja egy IoT-rendszer **biztonsági vizsgálata** szimulált környezetben:

- MQTT alapú kommunikáció ESP32 szenzorok és broker között  
- titkosítatlan vs. TLS-sel védett MQTT összehasonlítása  
- később mTLS + ACL alapú védelem és támadási szcenáriók modellezése  
- a hatás mérhető elemzése (üzenetráta, elutasított kapcsolatok stb.)

---

## Könyvtárstruktúra

```text
.
├── irodalom/
│   ├── Szakdolgozat-vázlat.pdf       # A dolgozat részletes vázlata
│   ├── irodalomjegyzek.pdf          # Irodalomjegyzék / források
│   └── szakdolgozat_iot_.pdf        # A szakdolgozat aktuális PDF verziója
│
├── kod/
│   ├── analyze_measurements.py      # Baseline (titkosítatlan) mérések elemzése
│   ├── analyze_measurements_tls.py  # TLS-es mérések elemzése
│   ├── ca.crt                       # Saját CA tanúsítvány (broker ellenőrzéséhez)
│   ├── collector.py                 # MQTT collector titkosítatlan brokerhez (1883)
│   ├── collector_tls.py             # MQTT collector TLS-es brokerhez (8883)
│   ├── measurements.csv             # Példa mérési adatok baseline futásból
│   ├── measurements_tls.csv         # Példa mérési adatok TLS-es futásból
│   ├── pub_test.py                  # Teszt/támadó kliens plaintext MQTT-hez
│   ├── pub_test_tls.py              # Teszt/támadó kliens TLS felett
│   └── subscriber.py                # Egyszerű MQTT subscriber (debug / demo célra)
│
└── wokdi_sensorok/
    ├── sensor1/
    │   └── sketch.ino               # Wokwi ESP32 "sensor1" kódja (MQTT publisher)
    └── sensor2/
        └── sketch.ino               # Wokwi ESP32 "sensor2" kódja (MQTT publisher)
