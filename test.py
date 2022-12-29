import numpy as np
import matplotlib.pyplot as plt

# Set the center of the circle
center = 1 - 1j

# Set the radius of the circle
radius = 1

# Create an array of angles from 0 to 2*pi
angles = np.linspace(0, 2*np.pi, 100)

# Calculate the x and y coordinates of the points on the circle
xs = radius * np.cos(angles) + center.real
ys = radius * np.sin(angles) + center.imag

# Plot the circle
plt.plot(xs, ys)

# Add labels and show the plot
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.title('Set of points z such that |z - (1 + i)| = 1')
plt.show()
