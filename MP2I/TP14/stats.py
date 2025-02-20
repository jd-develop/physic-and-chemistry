#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
import numpy as np

# l-l_0 en fonction de m
# avec D = 242.5 cm
m = np.array([0, 10, 20, 40, 50, 100, 150])*(1e-3)  # grammes
lml0 = np.array([0, 0.5, 0.9, 1.8, 2.1, 4.4, 6.2])*(1e-2)  # centimètres

a, b = np.polyfit(m, lml0, 1)

plt.plot(m, lml0, "ro")
x = np.linspace(0, 0.15, 150)
plt.plot(x, a * x + b)
plt.text(0, 0.05, f"l-l_0 = {round(a, 5)}m + {round(b, 5)}")
plt.xlabel("m en kg")
plt.ylabel("l-l_0 en m")
plt.grid(True)
plt.show()

