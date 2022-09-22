#!/usr/bin/env python3
# coding:utf-8
from matplotlib import pyplot as plt

elements_on_earth = {
    "O": 48.8,
    "Mg": 16.5,
    "Fe": 14.3,
    "Si": 13.8,
    "S": 3.7,
    "Al": 1.6,
    "Ni": 0.8,
    "Cr": 0.2,
    "H": 0.2,
    "N": 0.004,
    "C": 0.002
}

plt.bar(elements_on_earth.keys(), elements_on_earth.values())
plt.title("Repartition of the chemical elements on the earth (%)")
plt.show()
