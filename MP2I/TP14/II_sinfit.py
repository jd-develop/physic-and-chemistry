#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def sinus(t, A, omega, phi, c):
    """
    La fonction sinus avec amplitude, pulsation, phase initiale et décalage,
    que l’on va donner à curve_fit pour qu’il puisse trouver les bonnes valeurs
    pour A, ω, φ et c.
    """
    return A*np.sin(omega*t + phi) + c


def plot_data_and_sinfit(file: str, first_guess, offset: float = 0):
    """
    first_guess correspond aux valeurs qu’on peut deviner à première vue
    de A, omega, phi et c (elles serviront de point de départ à curve_fit)
    """
    with open(file, "r", encoding="UTF-8") as fp:
        donnees_csv = fp.read().split("\n")

    donnees_csv.pop(0)
    if donnees_csv[-1] == "":
        donnees_csv.pop()

    donnees_csv_t = [float(s.split(",")[0]) for s in donnees_csv]
    donnees_csv_y = [float(s.split(",")[2]) + offset for s in donnees_csv]

    # on enlève les 15 premières valeurs car elles ont été mesurées avant le
    # lâcher
    aopc, _ = curve_fit(sinus, donnees_csv_t[15:], donnees_csv_y[15:], first_guess)
    a, omega, phi, c = aopc

    x = np.linspace(donnees_csv_t[15], donnees_csv_t[-1], 1000)
    courbe_approximée = [sinus(t, a, omega, phi, c) for t in x]

    plt.xlabel("t en secondes")
    plt.ylabel("aY en mètres par secondes au carré")

    plt.plot(donnees_csv_t, donnees_csv_y, '.')
    plt.plot(x, courbe_approximée)
    # plt.grid()
    plt.text(0, 2.5, f"aY = {a:.2f}sin({omega:.2f}t + {phi:.2f}) + {c:.2f}")


plot_data_and_sinfit("acceleration_sans_g.csv", (2.5, 2*np.pi/0.6, -np.pi/2, 0))
plt.show()

