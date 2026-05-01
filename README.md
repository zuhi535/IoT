# IoT Security Thesis Supplement

## Thesis title
**IoT Security: Identification of Attack Surfaces and Development of Defense Mechanisms**  
**Vulnerability Analysis of IoT Devices and Application of Secure Network Protocols**

## Purpose of the supplement
This supplement contains the source codes, measurement files, Wokwi projects, and additional documentation related to the practical part of the thesis.

The aim of the project is to simulate an MQTT-based IoT environment, compare unencrypted communication with communication protected by TLS 1.3, examine attack scenarios, and demonstrate a simple AI-based anomaly detection experiment.

## Environment used
- Operating system: Windows
- Python version: 3.9
- MQTT broker: Eclipse Mosquitto
- Simulation environment: Wokwi
- Virtual devices: ESP32

## Main parts of the supplement

### `szakdolgozat/`
Final thesis documents.
- `szakdolgozat_iot.pdf`
- `szakdolgozat_iot.odt`

### `forraskod/`
Python scripts used for the measurement backend, analysis, and additional examinations.
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
Results of measurements and test runs.
- `measurements.csv`
- `measurements_tls.csv`
- `measurements_normal.csv`
- `measurements_attack.csv`
- `measurements_attack_only.csv`

### `wokwi_sensorok/`
Two ESP32-based sensor projects executed in Wokwi.
- `sensor1/`
- `sensor2/`

### `dokumentacio/`
Additional documentation related to the supplement.
- `README.md`
- `requirements.txt`
- `futtatasi_lepesek.txt`

## Note
The project was created in a laboratory-based, simulated environment.  
The measurements and tests presented in the thesis were carried out under controlled conditions.
