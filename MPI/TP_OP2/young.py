#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np

τ = 3.96   # ms, interfrange
u_τ = np.sqrt(2/3) * 0.5  # largeur de l’intervalle de confiance : 1 ms
I = 9  # nombre d’interfranges

# total de la barette
d = 2048 * 14  # micromètres
T = 6.58  # ms

D = (190.8-35) * 10  # millimètres
λ = 650e-6  # millimètres

i = ((d*τ/T)/I)/1000  # largeur d’une interfrange
u_i = i * u_τ/τ
print(f"interfrange i = {i:.2f} ± {u_i:.2f} mm")  # millimètres

b = λ*D/i  # millimètres
u_b = b * u_τ/τ
print(f"écart entre les fentes b = {b:.2f} ± {u_b:.2f} mm")

b_constructeur = 0.5  # millimètres
z_score = abs(b_constructeur-b)/u_b
print(f"Z-score : {z_score:.2f}")

