#!/usr/bin/env python3
# coding:utf-8
from matplotlib import pyplot as plt

elements_in_human_body = {
    "H": 9.5,
    "O": 60.1,
    "C": 23.9,
    "N": 3,
    "P": 1.2,
    "Ca": 1.5,
    "S": 0.24,
    "Na": 0.15,
    "K": 0.19,
    "Cl": 0.15,
    "Mg": 0.03,
}

plt.bar(elements_in_human_body.keys(), elements_in_human_body.values())
plt.title("Repartition of the chemical elements in a human body (% of the mass)")
plt.show()
