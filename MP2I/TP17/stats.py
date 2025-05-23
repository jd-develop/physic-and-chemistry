#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#type: ignore
import matplotlib.pyplot as plt
from math import sqrt

with open("mesures.csv", "r+", encoding="utf-8") as fp:
    contenu = fp.readlines()

if contenu[-1] == "\n":
    contenu.pop()

contenu.pop(0)

contenu_converted = [list(map(float, line.split(";"))) for line in contenu][90:100]

t = [l[0] for l in contenu_converted]
x = [l[1] for l in contenu_converted]
y = [l[3] for l in contenu_converted]

dt = t[1] - t[0]  # constante

vx = [(x[i+1] - x[i]) / dt for i in range(len(x) - 1)]
vy = [(y[i+1] - y[i]) / dt for i in range(len(y) - 1)]
ax = [(vx[i+1] - vx[i]) / dt for i in range(len(vx) - 1)]
ay = [(vy[i+1] - vy[i]) / dt for i in range(len(vy) - 1)]

def speed_vect(dt: float, i: int):
    plt.quiver(x[i], y[i], vx[i], vy[i], scale_units="xy", angles="xy", color="blue", width=0.005)
    plt.text(x[i]+0.20, y[i]+0.05, r"$\vec{v}$" + str(i), color="blue")
    speed = sqrt(vx[i]**2 + vy[i]**2)
    print(f"À la position {i}, la vitesse est de {round(speed, 2)} m/s")
    
plt.plot(x, y, "ro")
for i in range(len(x)-1):
    speed_vect(x, y, dt, i)
plt.xlabel("Position x")
plt.ylabel("Position y")
plt.grid()
plt.show()
