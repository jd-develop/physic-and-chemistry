#!/usr/bin/env python3
# coding:utf-8
from matplotlib import pyplot as plt

elements_in_universe = {
    "H": 90,
    "He": 9,
    "O": 0.1,
    "C": 0.06,
    "Ne": 0.012,
    "N": 0.01,
    "Mg": 0.005,
    "Si": 0.005,
    "Fe": 0.004,
    "S": 0.002
}

plt.bar(elements_in_universe.keys(), elements_in_universe.values())
plt.title("Repartition of the chemical elements in the universe (% of the matter)")
plt.show()
