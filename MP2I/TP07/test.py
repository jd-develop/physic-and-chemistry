import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from colour import SpectralDistribution, XYZ_to_sRGB, sd_to_XYZ

# Your data
lambda1 = np.array([404.7, 407.8, 435.8, 491.6, 546.1, 577.0, 579.1, 690.7])
lambda1 *= 1e-9
theta1 = np.array([137+29/60, 137 + 17/60, 135+16/60, 134+11/60, 132+7/60, 131, 130.5+22/60, 129+9/60])
thetam1 = np.array([165.5+23/60, 166.35, 167, 169, 170.5+28/60, 172+2/60, 172+10/60, 173.5+16/60])
theta1 = theta1 - 151.5-19/60
thetam1 = thetam1 - 151.5-19/60
alpha = (thetam1 - theta1)/2

# Fit the data
a, b = np.polyfit(lambda1, np.sin(np.radians(alpha)), 1)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(lambda1, np.sin(np.radians(alpha)), "ro")
ax.plot(np.linspace(4e-7, 7e-7, 100), a * np.linspace(4e-7, 7e-7, 100) + b)
ax.text(5e-7, 0.26, f"sin(θ) = {a:.0f}λ {b:.4f}")
ax.set_ylabel("sin(θ)")
ax.grid(True)

# Remove the original x-axis labels and ticks
ax.xaxis.set_ticklabels([])
ax.xaxis.set_ticks_position('none')

def wavelength_to_rgb(wavelength):
    """
    Convert a wavelength in nanometers to an RGB color.
    """
    sd = SpectralDistribution({wavelength: 1.0})
    XYZ = sd_to_XYZ([sd])
    RGB = XYZ_to_sRGB(XYZ)
    return RGB
# Get the minimum and maximum values of the x-axis
xmin, xmax = ax.get_xlim()
wavelengths = np.linspace(xmin*1e9, xmax*1e9, 100)  # Wavelengths in nanometers
colors = np.array([wavelength_to_rgb(wavlgth) for wavlgth in wavelengths])

# Create a color map and color bar
cmap = mcolors.ListedColormap(colors.reshape(-1, 3))
norm = mcolors.Normalize(vmin=xmin, vmax=xmax)
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([wavelengths])

# Create a new axis for the color bar that matches the x-axis range
pos = ax.get_position()
cbar_ax = fig.add_axes([pos.x0, pos.y0, pos.width, 0.02])  # [left, bottom, width, height]
cbar = fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')
cbar.set_label('λ en m')
plt.show()
