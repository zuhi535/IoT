import sys
import json

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix


def load_measurements(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    if not {"recv_time", "topic", "payload"}.issubset(df.columns):
        raise ValueError("A CSV-nek tartalmaznia kell a 'recv_time', 'topic', 'payload' oszlopokat.")

    df["recv_time"] = pd.to_datetime(df["recv_time"])

    sensor_ids = []
    temps = []
    ts_device = []

    for raw in df["payload"]:
        try:
            data = json.loads(raw)
        except Exception:
            data = {}

        sensor_ids.append(data.get("sensor_id", "unknown"))
        temps.append(data.get("temperature", np.nan))
        ts_device.append(data.get("ts_device", np.nan))

    df["sensor_id"] = sensor_ids
    df["temperature"] = temps
    df["ts_device"] = ts_device

    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["sensor_idx"] = df["sensor_id"].astype("category").cat.codes

    df = df.sort_values(["sensor_id", "recv_time"]).copy()
    df["delta_t"] = (
        df.groupby("sensor_id")["recv_time"]
        .diff()
        .dt.total_seconds()
    )

    median_dt = df["delta_t"].median()
    df["delta_t"] = df["delta_t"].fillna(median_dt)

    return df


def train_isolation_forest(df_normal: pd.DataFrame):
    df_normal = add_features(df_normal)
    train = df_normal.dropna(subset=["temperature"]).copy()

    X_train = train[["sensor_idx", "temperature", "delta_t"]].values

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42,
    )
    model.fit(X_train)
    return model


def predict_anomalies(model, df: pd.DataFrame) -> pd.DataFrame:
    df = add_features(df)
    test = df.dropna(subset=["temperature"]).copy()

    X_test = test[["sensor_idx", "temperature", "delta_t"]].values
    preds = model.predict(X_test)

    test["is_anomaly"] = (preds == -1).astype(int)
    return test


def main():
    if len(sys.argv) != 3:
        print("Használat: py -3.9 ml_anomaly_detector.py measurements_normal.csv measurements_attack.csv")
        sys.exit(1)

    path_normal = sys.argv[1]
    path_attack = sys.argv[2]

    print(f"[+] Normál adat: {path_normal}")
    print(f"[+] Támadásos adat: {path_attack}")

    df_normal = load_measurements(path_normal)
    df_attack = load_measurements(path_attack)

    print("[+] IsolationForest tanítása normál adaton...")
    model = train_isolation_forest(df_normal)

    print("[+] Anomáliák jelölése a támadásos adaton...")
    test = predict_anomalies(model, df_attack)

    test["label_true"] = (
        test["sensor_id"].astype(str).str.lower() == "attack"
    ).astype(int)

    print("\n=== Rövid statisztika ===")
    print(test[["recv_time", "sensor_id", "temperature", "delta_t", "is_anomaly", "label_true"]].head(20))

    print("\n=== Ellenőrzés ===")
    print("sensor_id előfordulások:")
    print(test["sensor_id"].value_counts(dropna=False))
    print("temperature tartomány:", test["temperature"].min(), "–", test["temperature"].max())

    if test["label_true"].sum() > 0:
        print("\n=== Teljesítmény (sensor_id == 'attack' alapján) ===")
        print(confusion_matrix(test["label_true"], test["is_anomaly"]))
        print(classification_report(test["label_true"], test["is_anomaly"]))
    else:
        print("\n[!] Nem találtunk 'attack' sensor_id-jú sort a measurements_attack.csv fájlban.")
        print("    Ez azt jelenti, hogy a fájlban nincs külön címkézett támadó üzenet.")


if __name__ == "__main__":
    main()