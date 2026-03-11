#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np
from matplotlib import pyplot as plt

L = 0.30  # mètres
# Aluminium
λ = 237  # Watt par mètre par Kelvin
ρ = 2698.9  # kilogrammes par mètre cube
c = 900  # Joule par kilogramme par Kelvin
dt = 0.1  # secondes
dx = 0.005  # mètres

T_0 = 300
ΔT = 20

D = λ/(ρ*c)
τ = L*L/D
t_1 = int(τ)
t_2 = 3*int(τ)
t_max = 10*int(τ)

X = np.array([i*dx for i in range(int(L/dx))])

# tableau de la température en fonction du temps (contient des tableaux de la
# température à un instant donné en fonction de la longueur)
temp = np.zeros((t_max, int(L/dx)))

temp[0] = (T_0 + ΔT*np.sin((np.pi/L) * X))  # T(x, 0)

for t in range(t_max-1):
    temp[t+1][0] = T_0
    temp[t+1][-1] = T_0
    for i in range(1, int(L/dx)-1):
        temp[t+1][i] = \
            dt * D * (temp[t][i+1] + temp[t][i-1] - 2*temp[t][i])/(dx**2) + temp[t][i]


plt.plot(X, temp[0])
plt.plot(X, temp[t_1-1])
plt.plot(X, temp[t_2-1])
plt.plot(X, temp[t_max-1])
plt.grid()
plt.show()

