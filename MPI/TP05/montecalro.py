#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import math

N = 100000

ures = math.radians(0.5)/math.sqrt(3)
urep = math.radians(1)/math.sqrt(3)
utot = math.sqrt(ures**2+urep**2)


def N_valeurs_de_a(a: float, u_a: float):
    return [np.random.uniform(a-u_a, a+u_a) for _ in range(N)]


def montecarlo(a: float, u_a: float):
    valeurs = N_valeurs_de_a(a, u_a)
    valeurs_f = [math.tan(v) for v in valeurs]

    moyenne = sum(valeurs_f)/len(valeurs_f)
    ecart_type = np.std(valeurs_f)

    return moyenne, ecart_type


print(*montecarlo(math.radians(20), utot))

