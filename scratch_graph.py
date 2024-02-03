import matplotlib.pyplot as plt
from scipy import stats

x = ["Smooth", "320", "120", "60"]
average = [54.75, 77.25, 84.5, 81.75]
std = [10.89437928, 5.629165125, 4.716990566, 2.861380786]
smooth = [
    58,
    70,
    51,
    40,
]
s_320 = [
    86,
    71,
    78,
    74,
]
s_120 = [
    84,
    83,
    79,
    92,
]
s_60 = [
    80,
    78,
    84,
    85,
]
y_points = [smooth, s_320, s_120, s_60]
x_points = []
for name in x:
    for i in range(4):
        x_points.append(name)
fig, ax = plt.subplots()
fontsize = 20
ax.set_ylabel("Pixel Brightness", fontsize=fontsize)
ax.set_xlabel("Salt Types", fontsize=fontsize)
ax.tick_params(labelsize=fontsize)
tukey = stats.tukey_hsd(smooth, s_320, s_120, s_60)
pvalues = tukey.pvalue
print(pvalues)


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
        ax.text((end + start) / 2, y, sig_text, fontsize=fontsize)
        ax.arrow(start, y, end - start, 0)
        ax.arrow(end, y, 0, -1)
        ax.arrow(start, y, 0, -1)


ax.bar(
    x,
    average,
    color="steelblue",
    yerr=std,
    align="center",
    alpha=1,
    ecolor="black",
    capsize=10,
)
ax.scatter(
    [name for name in x for i in range(4)],
    [point for cat in y_points for point in cat],
    color="red",
    alpha=0.5,
)
for i in range(1, 4):
    signif_line_draw(0, i, 100 + (i * 7), pvalues[0][i])
for i in range(2, 4):
    signif_line_draw(1, i, 90 + (i * 7), pvalues[1][i])
signif_line_draw(2, 3, 80, pvalues[2][-1])
ax.set_ylabel("Pixel Brightness")
ax.set_xlabel("Sandpaper Grit")
plt.show()
