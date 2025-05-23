import matplotlib.pyplot as plt
import numpy as np

# I = 1.64  :;A

longueur = np.array([0, 4, 8, 12, 16, 18, 20, 22])

Bx_a =  np.array([1.31, 1.31, 1.31, 1.29, 1.26, 1.20, 1.03, 0.62])
Bx_b = np.array([1.28, 1.31, 1.31, 1.29, 1.26, 1.20, 1.02, 0.60])

plt.plot(longueur, Bx_a, "ro")
plt.plot(longueur, Bx_b, "bo")
plt.show()