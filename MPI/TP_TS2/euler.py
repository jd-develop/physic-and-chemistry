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

    omega_0 = math.tau*f_c  # τ=2π

    # précalcul du facteur devant v_e dans l’expression de s_(n+1)
    facteur1 = -1/f_e * (R_2/R_1) * omega_0
    # précalcul du facteur devant s_n dans l’expression de s_(n+1)
    facteur2 = 1 - (1/f_e)*omega_0


    for v in v_e:
        s_n_plus_1 = facteur1*v + facteur2*s_n
        v_s_1.append(s_n_plus_1)
        s_n = s_n_plus_1

    return v_s_1


def calcul_v_s_0_pour_ce_filtre(f: int | float, f_c: int | float):
    """Cette fonction calcule v_s(0) pour notre filtre en particulier.
       f est la fréquence du signal d’entrée. On considère que v_e est un sinus.
    """
    gain = (R_2/R_1)/math.sqrt(1+(f/f_c)**2)
    phi = math.atan(f/f_c)
    return gain*math.sin(phi)


print(FRÉQUENCE_COUPURE)
sinus_100_hz = [math.sin(math.tau*(100)*(t/1e4)) for t in range(500)]
sinus_100_hz_amplifié = [10*math.sin(math.tau*(100)*(t/1e4)) for t in range(500)]
sinus_1_khz = [math.sin(math.tau*(1e3)*(t/1e5)) for t in range(500)]
sinus_freq_coupure = [math.sin(OMEGA_0*(t/1e5)) for t in range(500)]
sinus_10_khz = [math.sin(math.tau*(10e3)*(t/1e6)) for t in range(500)]
sinus_100_khz = [math.sin(math.tau*(100e3)*(t/1e7)) for t in range(500)]

v_s_0_1 = calcul_v_s_0_pour_ce_filtre(100, FRÉQUENCE_COUPURE)
plt.plot(range(500), sinus_100_hz_amplifié, label="Entrée")  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_100_hz, v_s_0_1, 1e4, FRÉQUENCE_COUPURE), label="Sortie")  # type: ignore
plt.title("Fréquence : 1 hHz (l’amplitude du signal d’entrée est exagérée d’un facteur 10 pour être visible)")  # type: ignore
plt.legend()  # type: ignore
plt.grid()  # type: ignore
plt.show()  # type: ignore

v_s_0_2 = calcul_v_s_0_pour_ce_filtre(1000, FRÉQUENCE_COUPURE)
plt.plot(range(500), sinus_1_khz, label="Entrée")  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_1_khz, v_s_0_2, 1e5, FRÉQUENCE_COUPURE), label="Sortie")  # type: ignore
plt.title("Fréquence : 1 kHz")  # type: ignore
plt.legend()  # type: ignore
plt.grid()  # type: ignore
plt.show()  # type: ignore

v_s_0_3 = calcul_v_s_0_pour_ce_filtre(FRÉQUENCE_COUPURE, FRÉQUENCE_COUPURE)
plt.plot(range(500), sinus_freq_coupure, label="Entrée")  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_freq_coupure, v_s_0_3, 1e5, FRÉQUENCE_COUPURE), label="Sortie")  # type: ignore
plt.title(f"Fréquence de coupure : {FRÉQUENCE_COUPURE:.2f} Hz")  # type: ignore
plt.legend()  # type: ignore
plt.grid()  # type: ignore
plt.show()  # type: ignore

v_s_0_4 = calcul_v_s_0_pour_ce_filtre(10000, FRÉQUENCE_COUPURE)
plt.plot(range(500), sinus_10_khz, label="Entrée")  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_10_khz, v_s_0_4, 1e6, FRÉQUENCE_COUPURE), label="Sortie")  # type: ignore
plt.title("Fréquence : 10 kHz")  # type: ignore
plt.legend()  # type: ignore
plt.grid()  # type: ignore
plt.show()  # type: ignore

v_s_0_5 = calcul_v_s_0_pour_ce_filtre(100000, FRÉQUENCE_COUPURE)
plt.plot(range(500), sinus_100_khz, label="Entrée")  # type: ignore
plt.plot(range(501), euler_ordre_1_passe_bas(sinus_100_khz, v_s_0_5, 1e7, FRÉQUENCE_COUPURE), label="Sortie")  # type: ignore
plt.title("Fréquence : 100 kHz")  # type: ignore
plt.legend()  # type: ignore
plt.grid()  # type: ignore
plt.show()  # type: ignore
