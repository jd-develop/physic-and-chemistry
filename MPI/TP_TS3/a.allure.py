#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
import numpy as np

T = range(1000)

u_e = np.array([np.sin(t*.02) for t in T])
h = np.array([1 if (t%10) < 3 else 0 for t in T])

u_s = h*u_e

plt.plot(T, u_s)
plt.grid()
plt.show()
