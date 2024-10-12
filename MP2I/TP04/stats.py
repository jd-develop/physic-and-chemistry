#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import numpy as np

d = np.array([33.2, 47.5, 59.8, 70.9, 82.5, 93.5])
D = np.arange(90, 150, 10)
f = (D ** 2 - d ** 2) / (4 * D)

print(np.mean(f))
print(np.std(f))
print(np.std(f) / (6 ** 0.5))
