#!/usr/bin/env python3
# coding:utf-8
from matplotlib import pyplot as plt

elements_in_human_body = {
    "H": 61,
    "O": 24.1,
    "C": 12.8,
    "N": 1.4,
    "P": 0.25,
    "Ca": 0.24,
    "S": 0.05,
    "Na": 0.04,
    "K": 0.03,
    "Cl": 0.03,
    "Mg": 0.008,
}

plt.bar(elements_in_human_body.keys(), elements_in_human_body.values())
plt.title("Repartition of the chemical elements in a human body (% of the matter)")
plt.show()
