#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
import numpy as np

file = "acceleration_frottements2.csv"
with open(file, "r", encoding="UTF-8") as fp:
    donnees_csv = fp.read().split("\n")

donnees_csv.pop(0)
if donnees_csv[-1] == "":
    donnees_csv.pop()

donnees_csv_t = [float(s.split(",")[0]) for s in donnees_csv]
donnees_csv_y = [float(s.split(",")[2]) for s in donnees_csv]

def get_extremum(f, p):
	T = int(1999 / p)
	y_max = []
	t_max = []
	for i in range(p):
		j_m, y_m = f(enumerate(donnees_csv_y[i*T:(i+1)*T]), key=lambda x: x[1])
		y_max.append(abs(y_m))
		t_max.append(donnees_csv_t[i*T + j_m])

	return np.array(t_max), np.array(y_max)

t_max, y_max = get_extremum(max, 33)
t_min, y_min = get_extremum(min, 35)

def plot_graph():
	plt.plot(donnees_csv_t, donnees_csv_y, '.')
	plt.plot(t_max, y_max, "r.")
	plt.plot(t_min, -y_min, ".")

	plt.xlabel("t en secondes")
	plt.ylabel("aY en mètres par secondes au carré")
	plt.grid(True)
	plt.show()

def plot_reg():
	a1, b1 = np.polyfit(t_max, np.log(y_max), 1)
	a2, b2 = np.polyfit(t_min, np.log(y_min), 1)
	t = np.linspace(0, 20)

	plt.plot(t_max, np.log(y_max), "ro", label="maximum")
	plt.plot(t, a1 * t + b1, "-")
	plt.plot(t_min, np.log(y_min), "o", label="minimum")
	plt.plot(t, a2 * t + b2, "-")
	plt.text(0.1, -0.16, f"y = {a1:.5f}t + {b1:.5f}", c="b")
	plt.text(0.1, -0.26, f"y = {a2:.5f}t + {b2:.5f}", c="g")

	plt.xlabel("t en secondes")
	plt.ylabel("y = ln(a) avec a l'amplitude en m/s^2")
	plt.legend()
	plt.grid()
	plt.show()


plot_graph()
plot_reg()