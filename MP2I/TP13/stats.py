#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
import numpy as np

# i en fonction de d
# avec D = 242.5 cm
d = np.array([200, 300, 500])*(1e-6)  # micromètres
i = np.array([0.74, 0.5, 0.3])*(1e-2)  # centimètres

a_di, b_di = np.polyfit(1/d, i, 1)

plt.plot(1/d, i, "ro")
x = 1 / np.linspace(200e-6, 500e-6, 100)
plt.plot(x, a_di * x + b_di)
plt.text(2000, 0.007, f"i = {round(a_di,8)}/d + {round(b_di, 8)}")
plt.xlabel("1/d en 1/m")
plt.ylabel("i en m")
plt.grid(True)
plt.show()

# i en fonction de D
# avec d = 200 μm
D = np.array([30.5, 40.5, 65.5, 88.0, 115, 242.5])*(1e-2)  # centimètres
i = np.array([0.08, 0.12, 0.2, 0.28, 0.36, 0.74])*(1e-2)  # centimètres

a_Di, b_Di = np.polyfit(D, i, 1)

plt.plot(D, i, "ro")
plt.plot(np.linspace(30.5e-2, 242.5e-2, 500), a_Di * np.linspace(30.5e-2, 242.5e-2, 500) + b_Di)
plt.text(0.3, 7e-3, f"i = {round(a_Di, 6)}D - {abs(round(b_Di, 6))}")
plt.xlabel("D en m")
plt.ylabel("i en m")
plt.grid(True)
plt.show()

