#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import numpy as np

x = np.array(range(0,90,10))
y = np.array([0, 6, 13, 19, 25, 30, 35, 38, 40])
x = np.sin(np.radians(x))
y = np.sin(np.radians(y))

n = x[1:]/y[1:]

print("la moyenne est: ", np.mean(n))
print("l'écart type est: ", np.std(n))
