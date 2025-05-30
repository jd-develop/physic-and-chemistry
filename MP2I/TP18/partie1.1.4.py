#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import matplotlib.pyplot as plt
import numpy as np

# en mT
bx = np.array([1.31, 1.31, 1.30, 1.23, 1.12, 0.80, 0.46])
# distance en centimètres
d = np.array([40, 28, 20, 12, 8, 4, 1])
# nombre de spires
n = np.array([200, 140, 100, 60, 40, 20, 10])

# longueur/rayon
lr = d/0.25

plt.xlabel("Rapport longueur/rayon")
plt.ylabel("Champ magnétique (mT)")
plt.grid()
plt.plot(lr, bx)
plt.show()

plt.xlabel("Distance d’enroulement (cm)")
plt.ylabel("Champ magnétique (mT)")
plt.grid()
plt.plot(d, bx)
plt.show()
