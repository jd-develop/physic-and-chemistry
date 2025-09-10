#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np
from matplotlib import pyplot as plt

freq = np.array([0.05,    0.1,     0.2,   0.5,     1,      2,     5,       10,    20,   50,     100])  # kHz
v_e  = np.array([1.98,    1.98,    1.98,  1.98,    2.08,   1.96,  1.992,   1.950, 1.95, 1.950,  1.950])  # volt crête-à-crête
v_s  = np.array([19.89,   19.8,    19.7,  18.9,    16.562, 11.9,  5.84,    3.077, 1.55, 0.644,  0.360])  # volt crête-à-crête
phi  = np.array([-178,   -176,    -173,  -163,    -149.77, -128, -108.46, -100,  -96,  -96,    -96.5])  # degré

H = v_s/v_e
GdB = 20*np.log10(H)

plt.plot(freq, GdB)
plt.xscale("log")
plt.grid()
plt.show()

plt.plot(freq, phi)
plt.xscale("log")
plt.grid()
plt.show()

