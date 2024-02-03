import matplotlib.pyplot as plt
import numpy as np

fine = np.array([53.03, 62.79, 48.14, 56.45, 54.98, 63.77])
control = np.array([62.3, 72.56, 69.14, 69.14, 72.07, 76.46])
label = ["Fine", "Control"]

fig, ax = plt.subplots()
ax.tick_params(labelsize=20)
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


signif_line_draw(0, 1, 80, 0.0013)
plt.scatter([lab for lab in label for i in range(6)], list(fine) + list(control), c="r")
ax.set_xlabel("Crystal Type", fontsize=20)
ax.set_ylabel("Temp C After 20 Seconds", fontsize=20)
plt.show()
