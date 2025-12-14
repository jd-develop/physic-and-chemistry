#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np
from matplotlib import pyplot as plt

theta = np.radians([0, 10, 20, 30, 40, 50, 60, 70, 80])  # , 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])
vmes = np.array([23.9, 22.4, 20.0, 16.4, 12.5, 8.1, 4.7, 2.2, 0.4])  # , 0.3, 1.7, 4.3, 8.1, 12.5, 16.9, 20.1, 23.0, 24.3, 24.4])


def incertitude(mesure):
    return np.sqrt(((0.1/100) * mesure + 5*0.1)**2 + 0.2**2)/np.sqrt(3)

incertitudes_vmes = incertitude(vmes)
incertitude_cos2_theta = np.abs(2*np.sin(theta)*np.cos(theta)*(np.radians(2)/np.sqrt(3)))

cos2theta = np.cos(theta)**2
pfit = np.polyfit(cos2theta, vmes, 1)
a, b = pfit[0], pfit[1]
x=np.linspace(min(cos2theta), max(cos2theta), 1000)
plt.plot(x, a*x+b)
plt.errorbar(cos2theta, vmes, xerr=2*incertitude_cos2_theta, yerr=2*incertitudes_vmes, fmt='.')
plt.show()
