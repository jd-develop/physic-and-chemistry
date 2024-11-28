import matplotlib.pyplot as plt
from math import *

# =====================================================
# Initialisation des signaux (réels et échantillonnage)
X = []
Y = []
Y1 = []
Y2 = []
Y3 = []

# ===============================================
# 3 périodes d'échantillonnage différentes
T1 = 1 / 1.6e-3  # f1 = 1,6*10^-3 Hz
T2 = 1 / 3.3e-3  # f2 = 3,3*10^-3 Hz
T3 = 1 / 0.01    # f3 = 0,01 Hz

# ===============================================
# Périodes de la sinusoïde composant le signal
T = 2000

# ===============================================
# Initialisation des compteurs d'échantillonnage
c1 = T1
c2 = T2
c3 = T3

value_1 = value_2 = value_3 = value_4 = 0

for k in range(5000):
    # Signal réel
    X += [k]
    Y += [sin(2 * pi * k / T)]

    # Échantillonnage 1
    if c1 >= T1:  # Si on a atteint la période d'échantillonnage
        # On prélève une nouvelle valeur du signal
        value_1 = sin(2 * pi * k / T)
        c1 = 0
    c1 += 1
    Y1 += [value_1]

    # Échantillonnage 2
    if c2 >= T2:
        value_2 = sin(2 * pi * k / T)
        c2 = 0
    Y2 += [value_2]
    c2 += 1

    # Échantillonnage 3
    if c3 >= T3:
        value_3 = sin(2 * pi * k / T)
        c3 = 0
    Y3 += [value_3]
    c3 += 1

# ==============================================================================
# Affichage des échantillonnages

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y1, color="blue")
plt.title("T_échantillonnage = " + str(T1) + " s  T_min_signal = " + str(T) + " s")
plt.show()

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y2, color="green")
plt.title("T_échantillonnage = " + str(T2) + " s  T_min_signal = " + str(T) + " s")
plt.show()

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y3, color="black")
plt.title("T_échantillonnage = " + str(T3) + " s  T_min_signal = " + str(T) + " s")
plt.show()

# =====================================================================================
# =====================================================================================

# =====================================================
# Initialisation des signaux (réels et échantillonnage)
X = []
Y = []
Y1 = []
Y2 = []
Y3 = []
Y4 = []

# ===============================================
# 3 périodes d'échantillonnage différentes
T1 = 600
T2 = 300
T3 = 100
T4 = 2

# ===============================================
# Périodes des sinusoïdes composant le signal
T = 2000
T_bis = 200

# ===============================================
# Initialisation des compteurs d'échantillonnage
c1 = T1
c2 = T2
c3 = T3
c4 = T4

for k in range(5000):
    # Signal réel
    X += [k]
    Y += [sin(2 * pi * k / T) + 0.3 * sin(2 * pi * k / T_bis)]

    # Échantillonnage 1
    if c1 >= T1:  # Si on a atteint la période d'échantillonnage
        # Alors on prélève une nouvelle valeur du signal
        value_1 = sin(2 * pi * k / T) + 0.3 * sin(2 * pi * k / T_bis)
        c1 = 0
    c1 += 1
    Y1 += [value_1]

    # Échantillonnage 2
    if c2 >= T2:
        value_2 = sin(2 * pi * k / T) + 0.3 * sin(2 * pi * k / T_bis)
        c2 = 0
    Y2 += [value_2]
    c2 += 1

    # Échantillonnage 3
    if c3 >= T3:
        value_3 = sin(2 * pi * k / T) + 0.3 * sin(2 * pi * k / T_bis)
        c3 = 0
    Y3 += [value_3]
    c3 += 1

    # Échantillonnage 4
    if c4 >= T4:
        value_4 = sin(2 * pi * k / T) + 0.3 * sin(2 * pi * k / T_bis)
        c4 = 0
    Y4 += [value_4]
    c4 += 1

# ===========================================================
# Affichage des échantillonnages

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y1, color="blue")
plt.title("T_échantillonnage = " + str(T1) + " s  T_min_signal = " + str(T_bis) + " s")
plt.show()

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y2, color="green")
plt.title("T_échantillonnage = " + str(T2) + " s  T_min_signal = " + str(T_bis) + " s")
plt.show()

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y3, color="black")
plt.title("T_échantillonnage = " + str(T3) + " s  T_min_signal = " + str(T_bis) + " s")
plt.show()

plt.plot(X, Y, color="deeppink")
plt.plot(X, Y4, color="black")
plt.title("T_échantillonnage = " + str(T4) + " s  T_min_signal = " + str(T_bis) + " s")
plt.show()
