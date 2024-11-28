#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Méthode de Monte-Carlo pour calculer la précision de la résistance
# mesurée

import numpy as np
import numpy.random as rd

# valeurs numériques
# tensions en Volt et intensités en milliampère
tension = np.array([2.806, 3.255, 3.564, 3.782, 4.067, 4.341])
intensite = np.array([43.97, 35.07, 28.97, 24.65, 19.01, 13.53]) * 1e-3  # Convertir en Ampères
s_tension = tension * 0.001 + 2 * 0.001  # précision sur la tension
s_intensite = intensite * 0.005 + 1e-6  # précision sur l’intensité

N = 10000  # nombre de valeurs tirées aléatoirement

# u = Ri + 0
r_monte_carlo = []
E_monte_carlo = []

# Calcul de N valeurs à partir des valeurs calculées
for _ in range(N):
    tension_monte_carlo = tension + s_tension * rd.normal(0, 1, len(tension))
    intensite_monte_carlo = intensite + s_intensite * rd.normal(0, 1, len(intensite))
    r, E = np.polyfit(intensite_monte_carlo, tension_monte_carlo, 1)
    r_monte_carlo.append(r)
    E_monte_carlo.append(E)

# Calcul de la moyenne et de l’incertitude-type
r_moyenne = np.mean(r_monte_carlo)
r_incertitude_type = np.std(r_monte_carlo)
E_moyenne = np.mean(E_monte_carlo)
E_incertitude_type = np.std(E_monte_carlo)

print("Si U = a*I + b :")
print(f"La valeur moyenne de a est {r_moyenne:.6f} avec une incertitude-type de {r_incertitude_type:.6f}")
print(f"La valeur moyenne de b est {E_moyenne:.6f} avec une incertitude-type de {E_incertitude_type:.6f}")
