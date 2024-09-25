#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

x = np.array([])
y = np.array([0, 6, 13, 19, 25, 30, 35, 38, 40])

x = np.sin(np.radians(x))
y = np.sin(np.radians(y))

[a, b] = np.polyfit(x, y, 1)

plt.text(0.7,0, f"y = {round(a, 4)}x - {round(abs(b), 4)}")
plt.plot(x, a*x+b, "b:")
plt.plot(x, y, "ro")

plt.title("sin(r) en Fonction de sin(i)")
plt.xlabel("sin(i)")

plt.ylabel("sin(r)")
plt.show()
