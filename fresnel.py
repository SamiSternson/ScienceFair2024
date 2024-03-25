import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-90, 90, 100)
print(np.deg2rad(x))
y = (
    (np.tan(np.deg2rad(x) - np.arcsin(1.0003 * np.sin(np.deg2rad(x)) / 1.54)))
    / (np.tan(np.deg2rad(x) + np.arcsin(1.0003 * np.sin(np.deg2rad(x)) / 1.54)))
) ** 2
fig, ax = plt.subplots()
plt.xlim(-90, 90)
ax.grid()
ax.plot(x, y, c="r")
ax.set_xlabel("Angle of Incidence in Degrees", fontsize=14)
ax.set_ylabel("Reflectivity", fontsize=14)
ax.tick_params(labelsize=14)
plt.show()
