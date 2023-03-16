#!/usr/bin/env python3
# coding:UTF-8

import matplotlib.pyplot as plt

# valeurs de Y, t et de V
t = [0, 0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36, 0.40, 0.44, 0.48, 0.52, 0.56]
y = [0, 0.010, 0.026, 0.048, 0.077, 0.100, 0.117, 0.125, 0.121, 0.110, 0.09, 0.064, 0.039, 0.020, 0.005]
v = [1.57, 1.51, 1.40, 1.24, 1.00, 0.68, 0.39, 0.02, 0.22, 0.54, 0.84, 1.1, 1.32, 1.46, 1.54]

# calculs des valeurs de Ec
Ec = []
for i in range(len(v)):
    Ec = Ec + [0.5 * 0.1 * v[i] ** 2]

# calculs des valeurs de Epp:
Epp = []
for i in range(len(y)):
    Epp = Epp + [0.1 * 9.81 * y[i]]

assert len(Ec) == len(Epp)  # on souhaite éviter les erreurs

Em = []  # on initialise la liste des énergies mécaniques
for i in range(len(Ec)):  # pour chaque indice de 0 à la longueur de Ec / de Epp
    # on ajoute à la liste des énergies mécaniques la somme de l'énergie cinétique et de l'énergie potentielle de
    # pesanteur
    Em.append(Ec[i] + Epp[i])

# tracé des courbes Ec(t) et Epp(t):
plt.title("Ec(t),Epp(t)")
plt.xlabel('t(s)')
plt.ylabel('Energies (J)')
plt.plot(t, Epp, 'b--', label='Epp')
plt.plot(t, Ec, 'g--', label='Ec')
plt.plot(t, Em, 'r--', label='Em')

plt.legend()
plt.show()
plt.close()
