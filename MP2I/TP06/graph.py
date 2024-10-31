#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import matplotlib.pyplot as plt
import numpy as np

# Montage courte dérivation 4.7kΩ
# 4598.093797768125 5.737469325292383
uc = np.array([0, 2.972, 4.479, 5.985, -7.460, -8.966, -11.946])
ic = np.array([0, 0.645, 0.973, 1.302, -1.623, -1.952, -2.602])
ic = ic / 1000
# plt.plot(uc, ic, "o-")

# Montage longue dérivation 4.7kΩ
# 4612.385196900777 5.801329058443846
ul = np.array([0, 2.98, 4.489, 6, -8.988, -7.479, -6])
il = np.array([0, 0.645, 0.972, 1.3, -1.951, -1.624, -1.302])
il = il / 1000
# plt.plot(ul, il, "o-")

# Montage courte dérivation 50Ω
uc2 = np.array([0, -5.927, -4.433, -2.940, 2.953, 4.449, 5.944])
ic2 = np.array([0, -0.111, -0.083, -0.054, 0.055, 0.084, 0.112])

# Montage longue dérivation 50Ω
ul2 = np.array([0, -5.997, -4.487, -2.977, 2.979, 4.487, 5.998])
il2 = np.array([0, -0.112, -0.083, -0.054, 0.055, 0.084, 0.112])

# Montage courte dérivation 604kΩ
uc3 = np.array([0, -5.988, -4.481, -2.973, 2.974, 4.482, 5.989])
ic3 = np.array([0, -10.45, -7.80, -5.15, 5.25, 7.90, 10.55]) / 1e6  # Convertir en ampères

# Montage longue dérivation 604kΩ
ul3 = np.array([0, -5.988, -4.488, -2.979, 2.980, 4.490, 6.000])
il3 = np.array([0, -9.86, -7.36, -4.86, 4.96, 7.46, 9.95]) / 1e6  # Convertir en ampères

# Créer une figure avec plusieurs sous-graphiques
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

def add_text(ax, u, i, y):
	coef = np.polyfit(i, u, 1)
	ax.text(0, y, f"u = {round(coef[0], 0)}i - {abs(round(coef[1], 3))}")
# Tracer le premier graphique
axs[0, 0].plot(uc2, ic2, "o-")
axs[0, 0].set_title("Montage courte dérivation 50Ω")
axs[0, 0].set_xlabel("Tension (V)")
axs[0, 0].set_ylabel("Courant (A)")
axs[0, 0].grid(True)
add_text(axs[0, 0], uc2, ic2, -0.075)
# Tracer le deuxième graphique
axs[0, 1].plot(ul2, il2, "o-")
axs[0, 1].set_title("Montage longue dérivation 50Ω")
axs[0, 1].set_xlabel("Tension (V)")
axs[0, 1].set_ylabel("Courant (A)")
axs[0, 1].grid(True)
add_text(axs[0, 1], ul2, il2, -0.075)

# Tracer le troisième graphique
axs[1, 0].plot(uc3, ic3, "o-")
axs[1, 0].set_title("Montage courte dérivation 604kΩ")
axs[1, 0].set_xlabel("Tension (V)")
axs[1, 0].set_ylabel("Courant (A)")
axs[1, 0].grid(True)
add_text(axs[1, 0], uc3, ic3, -0.75e-5)

# Tracer le quatrième graphique
axs[1, 1].plot(ul3, il3, "o-")
axs[1, 1].set_title("Montage longue dérivation 604kΩ")
axs[1, 1].set_xlabel("Tension (V)")
axs[1, 1].set_ylabel("Courant (A)")
axs[1, 1].grid(True)
add_text(axs[1, 1], ul3, il3, -0.75e-5)

# Ajuster les espaces entre les sous-graphiques
plt.tight_layout()
plt.show()