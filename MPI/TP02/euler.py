#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
from matplotlib import pyplot as plt

R_1 = 1e3   # ohm
R_2 = 10e3  # ohm
R_3 = 10e3  # ohm
C = 10e-9   # farad

OMEGA_0 = 1/(R_2*C)
FRÉQUENCE_COUPURE = 1/(math.tau*R_2*C)  # τ=2π


def euler_ordre_1_passe_bas(
    v_e: list[int | float],
    v_s_0: int | float,
    f_e: int | float,
    f_c: int | float
) -> list[int | float]:
    """
    Renvoie une liste v_s_1 correspondant au signal de sortie, en utilisant
    la suite récurrente trouvée à la question 1.

    v_e est la liste des tensions d’entrée
    v_s_0 est la valeur initiale de la tension de sortie
    f_e = 1/T_c est la fréquence d’échantillonnage
    f_c est la fréquence de coupure du filtre
    """
    v_s_1 = [v_s_0]
    s_n = v_s_0

    # précalcul du facteur devant v_e dans l’expression de s_(n+1)
    facteur = -1/f_e * (R_2/R_1) * (math.tau*f_c)  # τ=2π

    for v in v_e:
        s_n_plus_1 = facteur*v + s_n
        v_s_1.append(s_n_plus_1)
        s_n = s_n_plus_1

    return v_s_1


print(FRÉQUENCE_COUPURE)
sinus_100_hz = [math.sin(math.tau*(100)*(t/1e4)) for t in range(500)]
sinus_100_hz_amplifié = [20*math.sin(math.tau*(100)*(t/1e4)) for t in range(500)]
sinus_1_khz = [math.sin(math.tau*(1e3)*(t/1e5)) for t in range(500)]
sinus_freq_coupure = [math.sin(OMEGA_0*(t/1e5)) for t in range(500)]
sinus_10_khz = [math.sin(math.tau*(10e3)*(t/1e6)) for t in range(500)]
sinus_100_khz = [math.sin(math.tau*(100e3)*(t/1e7)) for t in range(500)]

plt.plot(range(500), sinus_100_hz_amplifié)  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_100_hz, 0, 1e4, FRÉQUENCE_COUPURE))  # type: ignore
plt.title("Fréquence : 1 hHz (l’amplitude du signal d’entrée est exagérée d’un facteur 20 pour être visible)")  # type: ignore
plt.show()  # type: ignore

plt.plot(range(500), sinus_1_khz)  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_1_khz, 0, 1e5, FRÉQUENCE_COUPURE))  # type: ignore
plt.title("Fréquence : 1 kHz")  # type: ignore
plt.show()  # type: ignore

plt.plot(range(500), sinus_freq_coupure)  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_freq_coupure, 0, 1e5, FRÉQUENCE_COUPURE))  # type: ignore
plt.title(f"Fréquence de coupure : {FRÉQUENCE_COUPURE:.2f} Hz")  # type: ignore
plt.show()  # type: ignore

plt.plot(range(500), sinus_10_khz)  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_10_khz, 0, 1e6, FRÉQUENCE_COUPURE))  # type: ignore
plt.title("Fréquence : 10 kHz")  # type: ignore
plt.show()  # type: ignore

plt.plot(range(500), sinus_100_khz)  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_100_khz, 0, 1e7, FRÉQUENCE_COUPURE))  # type: ignore
plt.title("Fréquence : 100 kHz")  # type: ignore
plt.show()  # type: ignore
