#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

# u en V et i en mA
r = np.array([50, 80, 110, 140, 200, 300])
u = np.array([2.806, 3.255, 3.564, 3.782, 4.067, 4.341])
i = np.array([43.97, 35.07, 28.97, 24.65, 19.01, 13.53]) * 1e-3

a, b = np.polyfit(i, u, 1)
plt.grid(True)
x = np.linspace(0.01353, 0.04397, 100)
plt.plot(x, a * x + b)
plt.plot(i, u, "ro")
plt.text(0.016, 2.9, f"y = {b:.4f} - {abs(a):.4f}x")
plt.ylabel("U (V)")
plt.xlabel("I (A)")
plt.show()
