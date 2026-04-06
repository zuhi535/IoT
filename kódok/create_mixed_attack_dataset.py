import pandas as pd

# Normál és támadó adatok beolvasása
df_normal = pd.read_csv("measurements_normal.csv")
df_attack = pd.read_csv("measurements_attack_only.csv")

# Egyesítés
df_mixed = pd.concat([df_normal, df_attack], ignore_index=True)

# Időbélyeg szerint rendezés
df_mixed["recv_time"] = pd.to_datetime(df_mixed["recv_time"], errors="coerce")
df_mixed = df_mixed.sort_values("recv_time")

# Új támadásos tesztfájl mentése
df_mixed.to_csv("measurements_attack.csv", index=False)

print("Kész: létrejött a measurements_attack.csv")
print("Normál sorok száma:", len(df_normal))
print("Attack sorok száma:", len(df_attack))
print("Összes sor:", len(df_mixed))