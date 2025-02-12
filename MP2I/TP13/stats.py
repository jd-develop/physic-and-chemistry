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

plt.plot(d, i, "ro")
plt.plot(np.linspace(200e-6, 500e-6, 100), a_di * 1/np.linspace(200e-6, 500e-6, 100) + b_di)
plt.text(250e-6, 7e-3, f"i = {a_di}/d + {b_di}")
plt.xlabel("d en m")
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
plt.text(0.3, 7e-3, f"i = {a_Di}D + {b_Di}")
plt.xlabel("D en m")
plt.ylabel("i en m")
plt.grid(True)
plt.show()

