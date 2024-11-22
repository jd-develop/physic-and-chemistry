#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

# première expérience
# angles mesurés
theta = np.array([151.5*60+17, 148.5*60+5, 145*60+26, 142*60+10, 155*60, 158*60+4, 161*60+15])
# on enlève l’angle pour p=0
theta = (-(theta - theta[0]))/60

# ordres
p = np.array([0, 1, 2, 3, -1, -2, -3])
pente = np.polyfit(p, np.sin(np.radians(theta)), 1)[0]

# deuxième expériences
lambda1 = np.array([404.7, 407.8, 435.8, 491.6, 546.1, 577.0, 579.1, 690.7])
lambda1 *= 1e-9  # millimètres
theta1 = np.array([137+29/60, 137 + 17/60, 135+16/60, 134+11/60, 132+7/60, 131, 130.5+22/60, 129+9/60])

thetam1 = np.array([165.5+23/60, 166.35, 167, 169, 170.5+28/60, 172+2/60, 172+10/60, 173.5+16/60])

theta1 = theta1 - 151.5-19/60
thetam1 = thetam1 - 151.5-19/60
alpha = (thetam1 - theta1)/2  # moyenne

a, b = np.polyfit(lambda1, np.sin(np.radians(alpha)), 1)
# plt.plot(p, np.sin(np.radians(theta)), "ro")
# plt.plot(np.linspace(-3, 3, 100), pente * np.linspace(-3, 3, 100))
plt.plot(lambda1, np.sin(np.radians(alpha)), "ro")
plt.plot(np.linspace(4e-7, 7e-7, 100), a * np.linspace(4e-7, 7e-7, 100) + b)
plt.text(5e-7, 0.26, f"sin(θ) = {a:.0f}λ {b:.4f}")
plt.xlabel("λ en m")
plt.ylabel("sin(θ)")
plt.grid(True)
plt.show()
