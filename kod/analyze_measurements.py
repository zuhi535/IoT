import csv
import json
from collections import defaultdict
from datetime import datetime


CSV_FILE = "measurements.csv"


def parse_row(row):
    """Egy CSV-sor feldolgozása: időbélyeg, sensor_id, hőmérséklet."""
    recv_time_str = row["recv_time"]
    topic = row["topic"]
    payload_str = row["payload"]

    try:
        recv_time = datetime.fromisoformat(recv_time_str)
    except ValueError:
        return None

    try:
        data = json.loads(payload_str)
    except json.JSONDecodeError:
        return None

    if not isinstance(data, dict):
        return None

    sensor_id = data.get("sensor_id", "unknown")
    temperature = data.get("temperature")

    return {
        "recv_time": recv_time,
        "topic": topic,
        "sensor_id": sensor_id,
        "temperature": temperature,
    }


def main():
    stats = defaultdict(
        lambda: {
            "count": 0,
            "temps": [],
            "first": None,
            "last": None,
        }
    )

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            parsed = parse_row(row)
            if parsed is None:
                continue

            sensor_id = parsed["sensor_id"]
            recv_time = parsed["recv_time"]
            temp = parsed["temperature"]

            s = stats[sensor_id]
            s["count"] += 1

            if isinstance(temp, (int, float)):
                s["temps"].append(temp)

            if s["first"] is None or recv_time < s["first"]:
                s["first"] = recv_time
            if s["last"] is None or recv_time > s["last"]:
                s["last"] = recv_time

    for sensor_id, s in stats.items():
        print(f"=== {sensor_id} ===")
        print(f"Üzenetek száma: {s['count']}")

        if s["first"] and s["last"] and s["last"] > s["first"]:
            duration = (s["last"] - s["first"]).total_seconds()
            rate = s["count"] / duration
            print(f"Időtartam: {duration:.1f} s")
            print(f"Becsült üzenetküldési ráta: {rate:.3f} msg/s")
        else:
            print("Időtartam: N/A")

        if s["temps"]:
            avg_temp = sum(s["temps"]) / len(s["temps"])
            print(f"Átlagos hőmérséklet: {avg_temp:.2f} °C")
        else:
            print("Nincsenek értelmezhető hőmérsékleti adatok.")
        print()


if __name__ == "__main__":
    main()
