#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
from math import tau
import numpy as np

M = 0.0501  # en kilogrammes
G = 9.81

def j(t_0: float, OG: float) -> float:
    return ((t_0**2) * M * G * OG)/(tau**2)

d = np.array([4.9, 5.4, 6.3, 6.6, 8.1]) * 1e-2  # en mètres
T_0 = np.array([6.2, 6.2, 6.4, 6.5, 6.6]) / 10  # en secondes

J_OΔ = [j(t_0, d[i]) for i, t_0 in enumerate(T_0)]
d2 = np.array(d)**2

a, b = np.polyfit(d2, J_OΔ, 1)
print(f"{a}x + {b}")
d2linspace = np.linspace(d2[0], d2[-1], 100)
J_OΔ_reglin = [a*x + b for x in d2linspace]

plt.plot(d2, J_OΔ, 'o')
plt.plot(d2linspace, J_OΔ_reglin)
plt.show()

