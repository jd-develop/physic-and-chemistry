#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np

m = np.array([0, 10, 20, 40, 50, 100, 150])*(1e-3)  # grammes
lml0 = np.array([0, 0.5, 0.9, 1.8, 2.1, 4.4, 6.2])*(1e-2)  # centimètres

um = 0.05  # incertitude relative, ne pas oublier de remultiplier !
ulml0 = 0.9e-2  # en centimètres

N = 10000

a_monte_carlo: list[int | float] = []
b_monte_carlo: list[int | float] = []
k_monte_carlo: list[int | float] = []

for i in range(N):
    m_mc = m + np.sqrt(3) * (um*m) * np.random.uniform(-1, 1, len(m))
    lml0_mc = lml0 + np.sqrt(3) * ulml0 * np.random.uniform(-1, 1, len(lml0))
    [a, b] = np.polyfit(m_mc, lml0_mc, 1)  # type: ignore
    a_monte_carlo.append(a)  # type: ignore
    b_monte_carlo.append(b)  # type: ignore
    k_monte_carlo.append(a*9.8)  # type: ignore

a_moyenne = np.average(a_monte_carlo)
u_a = np.std(a_monte_carlo)

b_moyenne = np.average(b_monte_carlo)
u_b = np.std(b_monte_carlo)

k_moyenne = np.average(k_monte_carlo)
u_k = np.std(k_monte_carlo)

print(f"Valeur moyenne de a : {a_moyenne}, incertitude-type : {u_a}")
print(f"Valeur moyenne de b : {b_moyenne}, incertitude-type : {u_b}")
print(f"Valeur moyenne de k : {k_moyenne}, incertitude-type : {u_k}")

