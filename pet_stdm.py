import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Imports data from files
data1 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/salt1.csv")
data2 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/salt2.csv")
data3 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/salt3.csv")
data4 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/salt4.csv")
data5 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/salt5.csv")
time = data1["Time"].tolist()
control1 = data1["Control"].tolist()
covered1 = data1["Covered"].tolist()
control2 = data2["Control"].tolist()
covered2 = data2["Covered"].tolist()
control3 = data3["Control"].tolist()
covered3 = data3["Covered"].tolist()
control4 = data4["Control"].tolist()
covered4 = data4["Covered"].tolist()
control5 = data5["Control"].tolist()
covered5 = data5["Covered"].tolist()
# Agregates lists
control = control1 + control2 + control3 + control4 + control5
covered = covered1 + covered2 + covered3 + covered4 + covered5

control_avg = []
covered_avg = []
control_stdm = []
covered_stdm = []
control_slope = linregress(time * 5, control)
covered_slope = linregress(time * 5, covered)
print(control_slope, covered_slope)
# Calculates the Standard Deviation of the Mean
for i in range(len(time)):
    control = np.array(
        [
            control1[i],
            control2[i],
            control3[i],
            control4[i],
            control5[i],
        ]
    )
    control_avg.append(np.mean(control))
    control_stdm.append(np.std(control) / np.sqrt(len(control)))

    covered = np.array(
        [covered1[i], covered2[i], covered3[i], covered4[i], covered5[i]]
    )
    covered_avg.append(np.mean(covered))
    covered_stdm.append(np.std(covered) / np.sqrt(len(covered)))

# Initiates graph
fig, ax = plt.subplots()
plt.xlim(1, 20)
plt.ylim(20, 55)


def abline(slope, intercept, color, linestyle):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color=color, alpha=1, linestyle=linestyle)


# Defines function that shades regions for Standard Deviation of the Mean
def graph_between(x, main_y, stdm_up, stdm_down, c, label):
    ax.plot(x, main_y, c=c, label=label)
    ax.plot(
        x,
        stdm_up,
        c=c,
        alpha=0.4,
    )
    ax.plot(
        x,
        stdm_down,
        c=c,
        alpha=0.4,
    )
    ax.fill_between(
        x,
        stdm_up,
        stdm_down,
        color=c,
        alpha=0.4,
    )


# Graph lines
graph_between(
    time,
    control_avg,
    [control_avg[i] + control_stdm[i] for i in range(len(control_avg))],
    [control_avg[i] - control_stdm[i] for i in range(len(control_avg))],
    "r",
    "Control",
)
graph_between(
    time,
    covered_avg,
    [covered_avg[i] + covered_stdm[i] for i in range(len(covered_avg))],
    [covered_avg[i] - covered_stdm[i] for i in range(len(covered_avg))],
    "b",
    "Finely ground crystals encased in PET",
)
fontsize = 16
ax.set_xticks(np.arange(2, 22, step=2))
ax.tick_params(labelsize=fontsize)
ax.plot(
    time,
    control_avg,
    "r",
)
ax.plot(
    time,
    covered_avg,
    "b",
)
abline(control_slope[0], control_slope[1], "r", "--")
abline(covered_slope[0], covered_slope[1], "b", "--")
ax.legend(loc="upper left", fontsize=fontsize - 4)
ax.set_xlabel("Time in Seconds", fontsize=fontsize)
ax.set_ylabel("Temp (C°)", fontsize=fontsize)
plt.title(
    "Temperature of copper plates covered in finely ground NaCl crystals\nencased in PET plastic during heating with IR lamp.",
    fontsize=12,
)
plt.show()
