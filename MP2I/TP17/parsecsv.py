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

contenu_converted = [list(map(float, line.split(";"))) for line in contenu]

t = [l[0] for l in contenu_converted]
x = [l[1] for l in contenu_converted]
y = [l[3] for l in contenu_converted]
v = [l[5] for l in contenu_converted]
a = [l[7] for l in contenu_converted]

def speed_vect(x: list[float], y: list[float], dt: float, i: int):
    vx = (x[i+1] - x[i]) / dt
    vy = (y[i+1] - y[i]) / dt
    plt.quiver(x[i], y[i], vx, vy, scale_units="xy", angles="xy", color="blue", width=0.005)
    plt.text(x[i]+0.20, y[i]+0.05, r"$\vec{v}$" + str(i), color="blue")
    speed = sqrt(vx**2+vy**2) 
    print(f"À la position {i} la vitesse est de {round(speed, 2)} m/s")

dt = t[1] - t[0] # constante

plt.plot(x, y, "ro")
speed_vect(x, y, dt, 0)
speed_vect(x, y, dt, len(t) // 2)
speed_vect(x, y, dt, len(t) - 2)
plt.xlabel("Position x")
plt.ylabel("Position y")
plt.grid()
plt.show()
