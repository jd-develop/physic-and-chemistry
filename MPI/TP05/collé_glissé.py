#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import lines
from matplotlib import animation

dt = 0.001

T_tot = 4
V = 0.1

M = 10
F_d = 0.3
F_s = 0.4
K = 4e3
g = 9.81

glissement = False

liste_temps: list[float] = [0]
liste_vitesses: list[float] = [0]
liste_positions: list[float] = [0]
liste_élongation: list[float] = [0]


def nouvel_état(glissement: bool, v: float, élongation: float) -> bool:
    if glissement and v <= 0:
        return False
    elif not glissement and K*élongation**2 > F_s*M*g:
        return True
    return glissement


while liste_temps[-1] < T_tot:
    glissement = nouvel_état(glissement, liste_vitesses[-1], liste_élongation[-1])
    if not glissement:
        liste_vitesses.append(0)
        liste_positions.append(liste_positions[-1])
        liste_élongation.append(liste_élongation[-1] + V*dt)
    else:
        # accélération = (v-v[-1])/dt donc v = accélération*dt + v[-1]
        # accélération = somme des forces = K*élongation² - F_d * mg
        acceleration = K*liste_élongation[-1]**2 - F_d * M * g
        liste_élongation.append(liste_élongation[-1] + V*dt - liste_vitesses[-1]*dt)
        liste_positions.append(liste_positions[-1] + liste_vitesses[-1]*dt)
        liste_vitesses.append(acceleration*dt + liste_vitesses[-1])
    liste_temps.append(liste_temps[-1]+dt)

plt.plot(liste_temps, liste_positions)
plt.grid()
plt.show()

plt.plot(liste_temps, liste_élongation)
plt.grid()
plt.show()


fig, ax = plt.subplots()
line1 = ax.plot([], [])[0]
line2 = ax.plot([], [], color="black")[0]
line3 = ax.plot([], [], color="black")[0]
line4 = ax.plot([], [], color="black")[0]
line5 = ax.plot([], [], color="black")[0]
support = ax.plot([-1, liste_positions[-1]+liste_élongation[-1]+1], [-0.012, -0.012])[0]
plt.xlim(-0.02, liste_positions[-1]+liste_élongation[-1]+0.02)
plt.ylim(-0.3, 0.3)

def animate(i: int):
    x = liste_positions[i]
    elongation = liste_élongation[i]
    line1.set_data([x,x+elongation], [0,0])
    line2.set_data([x, x-0.01], [-0.01, -0.01])
    line3.set_data([x, x-0.01], [0.01, 0.01])
    line4.set_data([x-0.01, x-0.01], [-0.01, 0.01])
    line5.set_data([x, x], [-0.01, 0.01])
    return support, line1, line2, line3, line4, line5

#for (x, elongation) in zip(liste_positions, liste_élongation):
#    frames.append(ax.plot([x, x+elongation], [1,1], color="blue"))

#anim = animation.ArtistAnimation(fig=fig, artists=frames, interval=dt)
#plt.show()

anim = animation.FuncAnimation(fig, animate, frames=int(T_tot/dt), interval=1,
                               blit=True, repeat=False)

plt.show()
