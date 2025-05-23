import matplotlib.pyplot as plt
import numpy as np

# intensitée du courant en Ampaire
I = np.array([0.00, 0.11, 0.23, 0.33, 0.44, 0.55, 0.67, 0.74, 0.91, 1.08, 1.19, 1.34, 1.42, 1.58, 1.64])
# mT
bx =  np.array([0.09, 0.16, 0.23, 0.29, 0.37, 0.44, 0.51, 0.55, 0.66, 0.76, 0.82, 0.91, 0.96, 1.06, 1.10])
bz = np.array([])

plt.plot(I, bx, "ro")
plt.show()