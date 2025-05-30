#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore

import matplotlib.pyplot as plt
import numpy as np

longueur = [0, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24]
moinslongueur = [-l for l in longueur]
moinslongueur.reverse()
bx = [1.00, 1.00, 1.00, 1.00, 1.01, 1.00, 0.99, 0.98, 0.96, 0.95, 0.92, 0.88, 0.81, 0.68, 0.48, 0.32, 0.21]
moinsbx = bx.copy()
moinsbx.reverse()

moinslongueur.extend(longueur)
moinsbx.extend(bx)

bz = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

plt.xlabel("Distance du teslamètre (cm)")
plt.ylabel("Champ magnétique (mT)")
plt.plot(moinslongueur, moinsbx)
plt.grid()
plt.show()
