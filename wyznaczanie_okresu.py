import pandas as pd
import numpy as np
from scipy.signal import find_peaks

# Wczytanie pliku Trackera
df = pd.read_csv(
    "wahadlo.csv",
    sep=r"\s+",
    decimal=",",
    header=None,
    names=["t", "x", "y"]
)

t = df["t"].to_numpy()
x = df["x"].to_numpy()

# Szukanie maksimów x(t)
peaks, _ = find_peaks(x, distance=80)

t_peaks = t[peaks]

# Okresy między kolejnymi amplitudami
periods = np.diff(t_peaks)

T = np.mean(periods)

print(f"Średni okres T = {T:.3f} s")

