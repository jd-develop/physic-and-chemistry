import matplotlib.pyplot as plt
import numpy as np

vs = np.array([121e-3, 173e-3, 410e-3, 650e-3, 1.29, 2.73, 4.7, 6.4, 7.2, 5.9, 3.70, 1.71, 1.15, 0.700, 0.360, 0.082, 0.025])

ve = np.array([10.5, 10.5, 10.5, 10.5, 10.3, 10.3, 9.8, 9.0, 8.6, 9.2, 10.1, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3])
# GBF par rapport à résistance en °
phi = np.array([-90, -87.84, -86.67, -85.61, -81.34, -70.30, -56.3, -32.66, -0.65, 43.68, 63.37, 80.13, 83.65, 88.20, 91.3, 93.1, 84.6]) * -1
#Hz
f = np.array([50, 100, 300, 500, 1e3, 2e3, 3e3, 4e3, 5e3, 7e3, 1e4, 2e4, 3e4, 5e4, 1e5, 3e5, 5e5])

plt.xscale("log")
plt.yscale("linear")
plt.xlabel("fréquence (Hz)")
plt.ylabel("Déphasage (°)")
# plt.plot(f, 20 * np.log10(vs/ve), "ro-")
plt.plot(f, phi, "ro-")
plt.grid(True, which="both")
plt.show()
