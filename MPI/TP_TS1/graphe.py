#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# type: ignore
from matplotlib import pyplot as plt
import math

t = [0.01*x for x in range(3140)]
sint = [math.sin(x) for x in t]
v_s = [1 if x>0 else -1 for x in sint]

plt.plot(t, sint, label="v_e")
plt.plot(t, v_s, '.', label="v_s")
plt.legend()
plt.show()
