#type: ignore
import matplotlib.pyplot as plt
from math import sqrt

def speed_vect(x: list[float], y: list[float], dt: float, i: int):
	vx = (x[i+1] - x[i]) / dt
	vy = (y[i+1] - y[i]) / dt
	plt.quiver(x[i], y[i], vx, vy, scale_units="xy", angles="xy", color="blue")
	plt.text(x[i]+0.20, y[i]+0.05, r"$\vec{v}$" + str(i), color="blue")
	speed = sqrt(vx**2+vy**2) 
	print(f"À la position {i} la vitesse est de {round(speed, 2)} m/s")

dt = 0.2
x = []
y = []