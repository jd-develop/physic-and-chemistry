#!/usr/bin/env python3
# -*- coding:utf-8 -*-

with open("mesures.csv", "r+", encoding="utf-8") as fp:
    contenu = fp.readlines()

if contenu[-1] == "\n":
    contenu.pop()

contenu.pop(0)

contenu_converted = [list(map(float, line.split(";"))) for line in contenu]

t = [l[0] for l in contenu_converted]
x = [l[1] for l in contenu_converted]
y = [l[3] for l in contenu_converted]
v = [l[5] for l in contenu_converted]
a = [l[7] for l in contenu_converted]

