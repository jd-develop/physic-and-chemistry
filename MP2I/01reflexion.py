#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
import numpy as np
from matplotlib import pyplot as plt

## Réflexion
x = np.array(range(0, 90, 10))
y = -x

[a, b] = np.polyfit(x, y, 1)

plt.plot(x, y, 'r.')
ymodel = a*x+b
plt.plot(x, ymodel)
plt.xlabel("i")
plt.ylabel("i’")
plt.title("Angle du rayon réfléchi i’ en fonction de l’angle l’incidence i.")
plt.text(10, 0, f"{a}x+{b}")
plt.show()

