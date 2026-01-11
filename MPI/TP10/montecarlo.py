#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np

N = 10000

a = 19.4 + 0.5*np.random.uniform(-1, 1, N)
ap = 118.3 + 0.05*np.random.uniform(-1, 1, N)

o1 = 45.95 + 0.15*np.random.uniform(-1, 1, N)
o2 = 90.95 + 0.45*np.random.uniform(-1, 1, N)

d1 = o1-a
d2 = o2-a
grand_d = ap-a

fp = (grand_d - ((d2-d1)**2)/grand_d)/4

print(f"f’ = {np.mean(fp):.2f} ± {np.std(fp):.2f}")

