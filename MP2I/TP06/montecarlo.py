#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Méthode de Monte-Carlo pour calculer la précision de la résistance
# mesurée

import numpy as np
import numpy.random as rd

# valeurs numériques
# tensions en Volt et intensités en milliampère
tension = np.array([-11.946, -8.966, -7.460, 2.972, 4.479, 5.985])
intensite = np.array([-2.602, -1.952, -1.623, 0.645, 0.973, 1.302])
s_tension   =   tension * 0.1 + 2*0.001  # précision sur la tension
s_intensite = intensite * 0.5 + (10**-6) # précision sur l’intensité
                                         # (10 digits avec comme unité 0.1 μA,
                                         # donc 0.1*10*10^-6 soit 10^-6)
N = 10000  # nombre de valeurs tirées aléatoirement

# u = Ri+0
r_monte_carlo: list[float] = []
zero_monte_carlo: list[float] = []

# Calcul de N valeurs à partir des valeurs calculées
for _ in range(N):
    tension_monte_carlo   = tension + s_tension * rd.uniform(-1, 1, len(tension))
    intensite_monte_carlo = intensite + s_intensite * rd.uniform(-1, 1, len(intensite))
    [r, zero] = np.polyfit(intensite_monte_carlo, tension_monte_carlo, 1)
    r_monte_carlo.append(r)
    zero_monte_carlo.append(zero)

# Calcul de la moyenne et de l’incertitude-type
r_moyenne = np.average(r_monte_carlo)
r_incertitude_type = np.std(r_monte_carlo)
zero_moyenne = np.average(zero_monte_carlo)
zero_incertitude_type = np.std(zero_monte_carlo)

print("Si U = a*I+b :")
print(f"La valeur moyenne de a est {round(r_moyenne, 2)} avec une incertitude-type de {round(r_incertitude_type, 2)}")
print(f"La valeur moyenne de b est {round(zero_moyenne, 2)} avec une incertitude-type de {round(zero_incertitude_type, 2)}")
