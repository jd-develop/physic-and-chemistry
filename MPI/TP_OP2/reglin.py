#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np
from matplotlib import pyplot as plt

d = [30, 40, 50, 60, 70, 80]  # centimètres
r = np.array([0.45+0.55, 0.6+0.7, 0.75+0.9, 0.9+1.1, 1.0+1.3, 1.15+1.5])/2  # largeur tache centrale, centimètres
u_r = (1/10) / (np.sqrt(2*3))
λ = 6.50e-5  # centimètres
largeur_fente_constructeur = 40

pente_list = []
b_list = []

for i in range(1000):
    new_r = r + np.random.uniform(-1, 1, len(r))*u_r
    pfit = np.polyfit(d, new_r, 1)
    a, b = pfit[0], pfit[1]
    pente_list.append(a)
    b_list.append(b)

pente, u_p = np.mean(pente_list), np.std(pente_list)
# print(pente, u_p)
x=np.linspace(min(d), max(d), 1000)

largeur_fente = (λ/pente)*(10**4)
u_a = (a * u_p/pente)*(10**4)
print(f"a = {largeur_fente:.2f}±{u_a:.2f} μm")

z_score = abs(largeur_fente_constructeur-largeur_fente)/u_a
print(f"Z-score : {z_score}")

plt.errorbar(d, r, xerr=0, yerr=u_r, fmt='.')
plt.plot(d, r, '.')
plt.plot(x, pente*x)
plt.show()

