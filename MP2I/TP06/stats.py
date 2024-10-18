#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

u = np.array([0, 2.97, 4.48, 5.99, -7.46, -8.97, -11.9])
i = np.array([0, 0.645, 0.974, 1.30, -1.62, -1.95, -2.60])
i = i / 1000
# R = u/i
# print(np.mean(R))
# print(np.std(R))

plt.plot(u, i, "o-")
# plt.plot(u, np.full(len(x), np.mean(R)), label="f'_moy")
plt.xlabel("U (V)")
plt.ylabel("I (A)")
plt.grid()
# plt.legend()
plt.show()
