#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt

def plot_file(file: str, offset: float = 0):
    # j’ai eu des expériences difficiles avec le module csv, je préfère
    # moi-même effectuer le parsing du fichier
    with open(file, "r", encoding="UTF-8") as fp:
        donnees_csv = fp.read().split("\n")

    donnees_csv.pop(0)
    if donnees_csv[-1] == "":
        donnees_csv.pop()

    donnees_csv_t = [float(s.split(",")[0]) for s in donnees_csv]
    donnees_csv_y = [float(s.split(",")[2]) + offset for s in donnees_csv]
    plt.xlabel("t en secondes")
    plt.ylabel("aY en mètres par secondes au carré")

    plt.plot(donnees_csv_t, donnees_csv_y, '.')


plot_file("acceleration_sans_g.csv")
plt.show()
plot_file("acceleration_avec_g.csv")
plt.show()
plot_file("acceleration_frottements1.csv")
plt.show()
plot_file("acceleration_frottements2.csv")
plt.show()

