import matplotlib.pyplot as plt
import numpy as np

# Data, x and y axes
fine = np.array([41.8, 40.82, 39.84, 38.38, 39.2])
control = np.array([58.4, 55.47, 50.59, 51.56, 50.49])

label = [
    "Finely ground crystals\nencased in PET plastic",
    "Control",
]
x = [0, 0.2]
fig, ax = plt.subplots()
ax.tick_params(labelsize=12)
# Graphs bars
barlist = ax.bar(
    x,
    [np.mean(fine), np.mean(control)],
    0.15,
    color="steelblue",
    yerr=[np.std(fine), np.std(control)],
    align="center",
    alpha=1,
    ecolor="black",
    capsize=10,
)
plt.xticks(x, label, fontsize=12)
barlist[-1].set_color("r")


# Function for lines of significance
def signif_line_draw(start, end, y, signif):
    insignificant = False
    if signif > 0.05:
        sig_text = ""
        insignificant = True
    elif signif <= 0.05 and signif > 0.01:
        sig_text = "*"
    elif signif < 0.01 and signif > 0.001:
        sig_text = "**"
    elif signif < 0.001 and signif > 0.0001:
        sig_text = "***"
    else:
        sig_text = "****"
    if not insignificant:
        ax.text((end + start) / 2, y, sig_text, fontsize=12)
        ax.arrow(start, y, end - start, 0)
        ax.arrow(end, y, 0, -1)
        ax.arrow(start, y, 0, -1)


# Draws line of significance
signif_line_draw(0, 0.2, 60, 0.000249)
# Labels axes and grpahs points
plt.scatter([lab for lab in x for i in range(5)], list(fine) + list(control), c="g")
ax.set_ylabel("Temp (C°) After 20 Seconds", fontsize=12)
plt.title(
    "Passive Cooling Effects of NaCl Crystals Encased in PET\non Copper Plates After 20 Seconds of Heating",
    fontsize=12,
)
plt.show()
