import numpy as np
import matplotlib.pyplot as plt

#Pomiary
L = np.array([0.75, 1.0, 1.25])
T = np.array([1.74, 2.01, 2.25])

# Wyznaczenie g
g = 4 * np.pi**2 * L / T**2
g_avg = np.mean(g)

# Symulacja
L_sim = np.linspace(0.1, 2.0, 500)
T_sim = 2 * np.pi * np.sqrt(L_sim / g_avg)

plt.figure(figsize=(8,8))
plt.plot(L_sim, T_sim, label=f"Model (g={g_avg:.2f} m/s²)")
plt.scatter(L, T, s=80, label="Pomiary")
plt.ylim(1.0, 2.8)
plt.yticks(np.arange(1.0, 2.8, 0.25))
plt.xlabel("Długość sznurka L [m]")
plt.ylabel("Okres T [s]")
plt.title("Okres drgań wahadła w funkcji długości")
plt.grid(True)
plt.legend()
plt.show()