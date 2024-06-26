import matplotlib.pyplot as plt
from scipy import stats

# Turning the data into variables
labels = ["Finely ground\ncrystals", "Table\nsalt", "Coarse\nsea salt"]
averages = [210, 182.6, 146.4]
std = [4.8, 6.1, 8.6]
fine = [204, 208, 211, 217, 208]
medium = [176, 181, 178, 188, 190]
coarse = [143, 143, 158, 152, 136]
data_points_y = [
    fine,
    medium,
    coarse,
]
width = 0.5
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
fontsize = 10
# Labeling Axes
ax.set_ylabel("Mean Pixel Brightness Indicating Reflectance", fontsize=fontsize)
ax.set_xlabel("Crystal Types", fontsize=fontsize)
ax.tick_params(labelsize=fontsize)

# Tuckey HSD test
tukey = stats.tukey_hsd(
    fine,
    medium,
    coarse,
)
# Creating Bar Graph
ax.bar(
    labels,
    averages,
    width,
    color="steelblue",
    yerr=std,
    align="center",
    alpha=1,
    ecolor="black",
    capsize=10,
)
# Showing data as scatter plot
ax.scatter(
    [name for name in labels for i in range(5)],
    [point for cat in data_points_y for point in cat],
    color="red",
    alpha=0.5,
)
pvalues = tukey.pvalue


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
        ax.text((end + start) / 2, y, sig_text, fontsize=fontsize)
        ax.arrow(start, y, end - start, 0)
        ax.arrow(end, y, 0, -1)
        ax.arrow(start, y, 0, -1)


# Draws lines of significance
for i in range(1, 3):
    signif_line_draw(0, i, 220 + (i * 12), pvalues[0][i])
for i in range(2, 3):
    signif_line_draw(1, i, 210 + (i * 7), pvalues[1][i])
signif_line_draw(2, 3, 180, pvalues[2][-1])
plt.title("IR Reflectance of Different\nParticle Size NaCl Crystals", fontsize=fontsize)
plt.show()
