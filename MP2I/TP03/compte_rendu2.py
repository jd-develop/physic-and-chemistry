#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

x = np.array([-100, -80, -60, -50, -40, -35, -11, -9, -7, 15, 20, 25, 30, 40, 50])
y = np.array([24.0, 25.7, 28.3, 31.6, 37.2, 52.5, -15.2, -17.5, -12.2, 8.4, 9.5, 10.5, 11.8, 12.8, 14.1])

x = 1/x
y = 1/y
[a, b] = np.polyfit(x, y, 1)

plt.text(0,-0.09, f"y = {round(a, 4)}x - {round(abs(b), 4)}")
plt.plot(x, a*x+b, "b:")
plt.plot(x, y, "ro")

plt.title("")
plt.xlabel("1/OA (cm^-1)")

plt.ylabel("1/OA' (cm^-1)")
plt.show()
