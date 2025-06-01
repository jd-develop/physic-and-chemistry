import matplotlib.pyplot as plt
import numpy as np

# u_0 en H.m^-1
u_0 = 4 * np.pi * 1e-7 
R = 6.5 * 1e-2
I = 1.98
# d = 4.4 cm
xa = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]) * 1e-2 + 0.01
xa = np.append(-xa[::-1], xa)
Bx_a =  np.array([3.32, 3.31, 3.18, 2.94, 2.61, 2.22, 1.82, 1.46, 1.17, 0.95, 0.76, 0.64, 0.44, 0.31]) * 1e-3
Bx_a = np.append(Bx_a[::-1], Bx_a)
# d = 6.5 cm
xb = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]) * 1e-2
xb = np.append(-xb[::-1], xb)
Bx_b = np.array([2.77, 2.77, 2.77, 2.70, 2.57, 2.28, 1.97, 1.61, 1.34, 0.88, 0.58]) * 1e-3
Bx_b = np.append(Bx_b[::-1], Bx_b)
# d = 19.5 cm
xc = np.array([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]) * 1e-2 -0.07 
xc = np.append(-xc[::-1], xc)
Bx_c = np.array([0.70, 0.74, 0.81, 0.91, 1.06, 1.26, 1.49, 1.74, 1.95, 2.05, 2.03, 1.85, 1.64, 1.34, 1.10, 0.88, 0.72]) * 1e-3
Bx_c = np.append(Bx_c[::-1], Bx_c)

x_continue = np.linspace(-0.16, 0.16, 100)
y_center = 0.00277
y_delta = 0.05 * y_center
plt.fill_between(x_continue, y_center - y_delta, y_center + y_delta, color="red", alpha=0.3, label="Tube des 5%")

plt.plot(xa, Bx_a, "o-", label="a")
plt.plot(xb, Bx_b, "o-", label="b")
plt.plot(xc, Bx_c, "o-", label="c")
plt.xlabel("abscisse en (m)")
plt.ylabel("champ magnétique en (T)")
plt.legend()
plt.show()