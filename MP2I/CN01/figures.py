#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

from matplotlib import pyplot as plt
import numpy as np

# constantes
n = 1.5
R = 5
y_lim = R/n
print(y_lim)

# les différentes ordonnées à l’origine des rayons incidents
# y_0 = [-4, -2, 0, 2, 4]
y_0 = np.linspace(-R, R, 20)

def abscisse(ordonnee):
    """Renvoie x_I en fonction de l’ordonnée y_I"""
    return np.sqrt(R**2 - ordonnee**2)

def angle_incidence(ordonnee):
    """Renvoie l’angle d’incidence en fonction de l’ordonnée de I"""
    return np.arcsin(ordonnee/R)

def angle_refracte(ordonnee):
    """Renvoie l’angle avec lequel le rayon réfracté repart en fonction
    de l’ordonnée de I. Renvoie None s’il n’existe pas"""
    if np.abs(ordonnee) > y_lim:
        return None
    return np.arcsin(n*angle_incidence(ordonnee))

def deviation(ordonnee):
    """Renvoie la déviation D en fonction de y_I, ou None si le rayon réfracté
    n’existe pas"""
    if np.abs(ordonnee) > y_lim:
        return None
    return angle_refracte(ordonnee) - angle_incidence(ordonnee)

def ordonnee_rayon_refracte(abscisse_M, y_I):
    """Renvoie l’ordonnée d’un point M d’abscisse `abscisse` situé sur le rayon
    réfracté, ou None si le rayon n’existe pas"""
    if np.abs(y_I) > y_lim:
        return None
    return y_I - (abscisse_M - abscisse(y_I)) * np.tan(deviation(y_I))

# ----- TRACÉ DE LA FIGURE À PROPREMENT PARLER -----
# dioptre d’entrée
plt.plot([0, 0], [-R, R], "k-")

# dioptre de sortie
yS = np.linspace(-R, R, 500)  # intervalle entre -R et R de 500 points
plt.plot(abscisse(yS), yS, "k-")

# tracé d’un rayon. Il faut 3 points : le point de départ en [-1, y], I en
# (i_I, y) et un point M par exemple de coordonnées (20, y_M)
for rayon in y_0:
    if np.abs(rayon) > y_lim:
        continue
    plt.plot([-1, abscisse(rayon), 20], [rayon, rayon, ordonnee_rayon_refracte(20, rayon)], "b-")

plt.axis("scaled")  # repère orthonormé
plt.show()

