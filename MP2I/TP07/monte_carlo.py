#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np

N = 100000
# longueurs d’onde étudiées
lambda1 = np.array([404.7, 407.8, 435.8, 491.6, 546.1, 577.0, 579.1, 690.7])
lambda1 *= 1e-9  # millimètres

# valeurs d’angle mesurées
theta1 = np.array([137+29/60, 137 + 17/60, 135+16/60, 134+11/60, 132+7/60, 131, 130.5+22/60, 129+9/60])
thetam1 = np.array([165.5+23/60, 166.35, 167, 169, 170.5+28/60, 172+2/60, 172+10/60, 173.5+16/60])

# on retire les angles de référence (ordre 0)
theta1 = theta1 - 151.5-19/60
thetam1 = thetam1 - 151.5-19/60

# on calcule la moyenne des deux valeurs
alpha = (thetam1 - theta1)/2
precision = 2/60  # précision de 2 minutes d’arc

n_mc: list[int | float] = []
for _ in range(N):
    alpha_mc = alpha + precision * np.random.normal(-1, 1, len(alpha))
    n_mc.append(np.polyfit(lambda1, np.sin(np.radians(alpha_mc)), 1)[0])

moyenne = np.average(n_mc)
incertitude = np.std(n_mc)
print(f"moyenne: {moyenne:.2f}, incertitude: {incertitude:.2f}")

