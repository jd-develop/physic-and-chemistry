#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

# I = 1.64 A

longueur = np.array([-22, -20, -18, -16, -12, -8, -4, 0, 4, 8, 12, 16, 18, 20, 22])

Bx_a =  np.array([0.62, 1.03, 1.20, 1.26, 1.29, 1.31, 1.31, 1.31, 1.31, 1.31, 1.29, 1.26, 1.20, 1.03, 0.62])
Bx_b = np.array([0.60, 1.02, 1.20, 1.26, 1.29, 1.31, 1.31, 1.28, 1.31, 1.31, 1.29, 1.26, 1.20, 1.02, 0.60])

plt.xlabel("Distance du teslamètre (cm)")
plt.ylabel("Champ magnétique (mT)")
plt.plot(longueur, Bx_a, "ro", label="Uniquement l’enroulement noir")
plt.plot(longueur, Bx_b, "bo", label="Enroulement noir en série avec l’enroulement rouge")
plt.grid()
plt.legend()
plt.show()
