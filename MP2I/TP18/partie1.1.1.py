import matplotlib.pyplot as plt
import numpy as np

longueur = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24])
bx =  np.array([1.00, 1.00, 1.00, 1.00, 1.01, 1.00, 0.99, 0.98, 0.96, 0.95, 0.92, 0.88, 0.81, 0.68, 0.48, 0.32, 0.21])
bz = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

plt.plot(longueur, bx)
plt.show()