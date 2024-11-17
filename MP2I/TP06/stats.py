import numpy as np

u = np.array([2.972, 4.479, 5.985, -7.460, -8.966, -11.946])
i = np.array([0.645, 0.973, 1.302, -1.623, -1.952, -2.602])
i = i / 1000
R = u/i
print(R)
print(f"la moyenne est {np.mean(R)} avec un écart type de: {np.std(R)}, et une insertitude de: {np.std(R) / np.sqrt(6)}")