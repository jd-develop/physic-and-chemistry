#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

x = np.array([-100, -80, -60, -50, -40, -35, -11, -9, -7, 15, 20, 25, 30, 40, 50])
y = np.array([24.0, 25.7, 28.3, 31.6, 37.2, 52.5, -15.2, -17.5, -12.2, 8.4, 9.5, 10.5, 11.8, 12.8, 14.1])

x = 1/x
y = 1/y

V = (y-x) * 10**2 #convertion cm^-1 en m^-1
f = 1/V
print(np.mean(f))
print(np.std(f))

plt.plot(1/x, f, "o-", label = "f'(OA)")
plt.plot(1/x, np.full(len(x), np.mean(f)), label="f'_moy")
plt.xlabel("OA (cm)")
plt.ylabel("f' (m)")
plt.legend()
plt.show()
