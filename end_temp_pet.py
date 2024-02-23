import matplotlib.pyplot as plt
import numpy as np

# Data, x and y axes
fine = np.array([41.8, 40.82, 39.84, 38.38, 39.2])
control = np.array([58.4, 55.47, 50.59, 51.56, 50.49])

label = ["Covered", "Control"]
fig, ax = plt.subplots()
ax.tick_params(labelsize=20)
# Graphs bars
ax.bar(
    label,
    [np.mean(fine), np.mean(control)],
    0.75,
    color="steelblue",
    yerr=[np.std(fine), np.std(control)],
    align="center",
    alpha=1,
    ecolor="black",
    capsize=10,
)


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
        ax.text((end + start) / 2, y, sig_text, fontsize=20)
        ax.arrow(start, y, end - start, 0)
        ax.arrow(end, y, 0, -1)
        ax.arrow(start, y, 0, -1)


# Draws line of significance
signif_line_draw(0, 1, 60, 0.000249)
# Labels axes and grpahs points
plt.scatter([lab for lab in label for i in range(5)], list(fine) + list(control), c="r")
ax.set_xlabel("Crystal Type", fontsize=20)
ax.set_ylabel("Temp C After 20 Seconds", fontsize=20)
plt.show()
