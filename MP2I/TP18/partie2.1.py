import matplotlib.pyplot as plt
import numpy as np

# u_0 en H.m^-1
u_0 = 4 * np.pi * 1e-7 
R = 6.5 * 1e-2
I = 1.98
x = np.array([-5.7, -4.5, -3, -2.5, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) * 1e-2 + 0.03
bx =  np.array([1.59, 1.78, 1.99, 1.95, 1.88, 1.71, 1.50, 1.23, 1.00, 0.82, 0.66, 0.53, 0.44, 0.35, 0.30, 0.25, 0.21, 0.17]) * 1e-3
B = u_0 * 95 * I * R * R / (2 * (R*R + x ** 2) ** (3/2))

plt.plot(x, bx, "ro-", label="exp")
plt.plot(x, B, label="theo")
plt.legend()
plt.show()