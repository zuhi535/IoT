# IoT Security szakdolgozati melléklet

## A szakdolgozat címe
**IoT security: támadási felületek azonosítása és védelmi mechanizmusok fejlesztése**  
**IoT eszközök sebezhetőségi elemzése, biztonságos hálózati protokollok alkalmazása**

## A melléklet célja
Ez a melléklet a szakdolgozat gyakorlati részéhez kapcsolódó forráskódokat, mérési állományokat, Wokwi-projekteket és kiegészítő dokumentációt tartalmazza.

A projekt célja egy MQTT-alapú IoT környezet szimulációja, a titkosítatlan és TLS 1.3-mal védett kommunikáció összehasonlítása, támadási szcenáriók vizsgálata, valamint egy egyszerű MI-alapú anomáliadetektálási kísérlet bemutatása.

## Használt környezet
- Operációs rendszer: Windows
- Python verzió: 3.9
- MQTT broker: Eclipse Mosquitto
- Szimulációs környezet: Wokwi
- Virtuális eszközök: ESP32

## A melléklet fő részei

### `szakdolgozat/`
A szakdolgozat végleges dokumentumai.
- `szakdolgozat_iot.pdf`
- `szakdolgozat_iot.odt`

### `forraskod/`
A mérési backendhez, elemzéshez és kiegészítő vizsgálatokhoz használt Python szkriptek.
- `collector.py`
- `collector_tls.py`
- `analyze_measurements.py`
- `analyze_measurements_tls.py`
- `pub_test.py`
- `pub_test_tls.py`
- `subscriber.py`
- `attack_publisher_tls.py`
- `create_mixed_attack_dataset.py`
- `ml_anomaly_detector.py`
- `ca.crt`

### `meresi_adatok/`
A mérési és tesztfuttatások eredményei.
- `measurements.csv`
- `measurements_tls.csv`
- `measurements_normal.csv`
- `measurements_attack.csv`
- `measurements_attack_only.csv`

### `wokwi_sensorok/`
A Wokwi-ban futtatott két ESP32-alapú szenzorprojekt.
- `sensor1/`
- `sensor2/`

### `dokumentacio/`
A melléklethez tartozó kiegészítő leírások.
- `README.md`
- `requirements.txt`
- `futtatasi_lepesek.txt`
Wokwi_sersor_1:https://wokwi.com/projects/449908585893820417 Wokwi_sersor_2:https://wokwi.com/projects/449908624240245761

## Megjegyzés
A projekt laboratóriumi, szimulált környezetben készült.  
A dolgozatban szereplő mérések és tesztek kontrollált környezetben történtek.
