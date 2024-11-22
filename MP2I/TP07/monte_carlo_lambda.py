#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import numpy.random as rd

# valeurs numériques
Dm = 20.6  # minimum de déviation
DmP = 2/60  # précision
N = 100000

DmMonteCarlo = Dm + DmP * rd.uniform(-1, 1, N)

lambdaMonteCarlo = (2*np.sin(np.radians(DmMonteCarlo/2)) / (600e3))*1e9  # (1e9 pour une valeur en nanomètres)

Lmoy = np.average(lambdaMonteCarlo)
incertitude_type = np.std(lambdaMonteCarlo)

print(f"La valeur moyenne de la longueur d’onde est de {Lmoy:.2f}")
print(f"L’incertitude-type est de {incertitude_type:.2f}")