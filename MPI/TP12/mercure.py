#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np
from matplotlib import pyplot as plt

# violet : 175° 0′, 404.7 nm
# (violet)
# indigo : 173° 31′, 435.8 nm
# (vert-bleu)
# vert : 170° 31′, 546.1 nm
# jaune 1 : 170° 2′, 576.1 nm
# jaune 2 : 170° 1', 579 nm
# (rouge)
# rouge : 169° 23′, 690.7 nm
# (rouge)

def degres(degre_minute):
    degres, minutes = degre_minute
    return degres + minutes/60

λ = np.array([404.7, 435.8, 546.1, 576.1, 579, 690.7])
Dmin = np.array(
    list(map(
        degres,
        [(175, 0), (173, 31), (170, 31), (170, 2), (170, 1), (169, 23)]
    ))
)

coeffs = np.polyfit(λ, Dmin, 4)
def polyn(x):
    return coeffs[0]*(x**4)+coeffs[1]*(x**3)+coeffs[2]*(x**2)+coeffs[3]*x+coeffs[4]

X = np.linspace(min(λ), max(λ), 100)
y = polyn(X)

plt.plot(X, y)
plt.plot(λ, Dmin)
plt.grid()
plt.show()
#expected 589
