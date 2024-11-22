#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import numpy as np
import matplotlib.pyplot as plt
# u en V et i en mA
r = np.array([50, 80, 110, 140, 200, 300])
u = np.array([2.806, 3.255, 3.564, 3.782, 4.067, 4.341])
i = np.array([43.97, 35.07, 28.97, 24.65, 19.01, 13.53]) * 1e-3

# print(np.mean(f))
# print(np.std(f))
print(np.polyfit(i, u, 1))
plt.plot(i, u)
plt.show()
