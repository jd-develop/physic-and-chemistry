#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
# Résolution de l’équation de Laplace à deux dimensions
import numpy as np
from matplotlib import pyplot as plt

L = 100

B = np.array([[False]*L for _ in range(L)])
for i in range(L):
    B[i][0] = True
    B[i][L-1] = True
    B[0][i] = True
    B[L-1][i] = True


def calculer_potentiels(v_init):
    v = np.copy(v_init)
    while True:
        nouveau_v = np.copy(v)
        equart_quadratique = 0
        for i in range(L):
            for j in range(L):
                if B[i][j]: continue
                nouveau_v[i][j] = (1/4) * (
                    v[i+1][j] + v[i-1][j] + v[i][j+1] + v[i][j-1]
                )
                equart_quadratique += (nouveau_v[i][j]-v[i][j]) ** 2
        v = nouveau_v
        print(equart_quadratique)
        if equart_quadratique <= 0.0001:
            break
    return v


def afficher_potentiels(v):
    # plt.imshow(v)
    # plt.colorbar()

    plt.contour(range(L), range(L), v, 10)
    plt.show()


v_init = np.zeros((L, L), dtype=float)
# for i in range(L):
#     v_init[i][0] = 1
#     v_init[i][L-1] = 1
#     v_init[0][i] = 1
#     # v_init[L-1][i] = 1
for i in range(80):
    B[40][10+i] = True
    v_init[40][10+i] = 3
    B[60][10+i] = True
    v_init[60][10+i] = -3
v = calculer_potentiels(v_init)
afficher_potentiels(v)


