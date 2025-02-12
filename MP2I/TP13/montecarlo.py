#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Méthode de Monte-Carlo pour calculer la précision de la vitesse des ultrasons
# mesurée

import numpy as np

N = 100000
# valeurs numériques
L = 8.8e-2
precision_L = 4e-3
freq = 40e3  # 40 kHz
precision_freq = 100

L_mc = np.random.normal(L, precision_L/np.sqrt(3), N)
f_mc = np.random.normal(freq, precision_freq/np.sqrt(3), N)
v_mc = (L_mc/10)*(f_mc)

moyenne = np.average(v_mc)
incertitude = np.std(v_mc)
print(f"moyenne: {moyenne}, incertitude: {incertitude}")

