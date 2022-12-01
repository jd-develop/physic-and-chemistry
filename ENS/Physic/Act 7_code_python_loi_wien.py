#!/usr/bin/env python3
# coding:utf-8
# Import des librairies utiles
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc
from math import *

# ==============================================================================
# Création des tableaux de données
invT = np.array([1 / 3955, 1 / 4755, 1 / 5716, 1 / 7536, 1 / 8263])  # Tableau des valeurs de 1/T avec T en Kelvins
lambda_ = np.array([0.73076, 0.60782, 0.50556, 0.38351, 0.34977])  # Tableau des valeurs des longueurs d'onde Lambda max

# ==============================================================================
# Tracé de la courbe expérimentale
plt.plot(invT, lambda_, linewidth=2, color="deeppink")
plt.xlabel("1/T avec T en Kelvin")  # Légende de l'abscisse.
plt.ylabel("λ max (µm)")  # Légende de l'ordonnée.
plt.title("Détermination de la loi de Wien : tracé de la courbe λ max = f(1/T)")
plt.grid()

# ==============================================================================
# Régression linéaire
droite = sc.linregress(invT, lambda_)  # Effectue une régression linéaire
coefficient = droite.slope  # On récupère la valeur du coefficient directeur de la droite.
print("Le coefficient directeur est : ", coefficient)
lambdaReg = coefficient * invT  # Calcule la valeur de lambda issue de la régression linéaire.

plt.plot(invT, lambdaReg, linewidth=2, color="black")  # Affichage de la régression linéaire.
plt.show()

constante_loi_de_wien = 2890.2064848576015

# ==============================================================================
# Courbe théorique
T_th = []
L_th = []
for t in range(3955, 8263):
    T_th.append(t)
    L_th.append(constante_loi_de_wien / t * 10 ** 9)

plt.plot(T_th, L_th)
plt.xlabel("Température T (en K)")  # Légende de l'abscisse.
plt.ylabel("Longueur d'onde lambda_max (en nm)")  # Légende de l'ordonnée.
plt.grid()
plt.show()

# ==============================================================================
# Courbe de la puissance surfacique solaire reçue dans le système solaire.
pSoleil = 38651e22  # Puissance totale émise par le soleil
d = []  # Liste des distances au soleil
P = []  # Liste des puissances reçues à une distance donnée du soleil.
for k in range(int(1e7), int(2.5e8), int(1e4)):  # On fait varier la distance par rapport au soleil, notée k ici.
    d.append(k)
    surfaceSphere = 4 * pi * k**2
    P.append(pSoleil / surfaceSphere)

plt.plot(d, P, linewidth=2, color="purple")
plt.xlabel("Distance au Soleil (en km)")
plt.ylabel("Puissance surfacique reçue (W.km-2)")
plt.grid()
plt.show()
