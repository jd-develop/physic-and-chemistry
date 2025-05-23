import matplotlib.pyplot as plt
import numpy as np

# en mT
bx = np.array([1.31, 1.31, 1.30, 1.23, 1.12, 0.80, 0.46])
# distance en centimètres
d = np.array([40, 28, 20, 12, 8, 4, 1])
# nombre de spires
n = np.array([200, 140, 100, 60, 40, 20, 10])

plt.plot(d, bx)
plt.show()