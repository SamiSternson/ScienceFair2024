import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

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
control = control1 + control2 + control3 + control4 + control5
covered = covered1 + covered2 + covered3 + covered4 + covered5
x = [t for i in range(5) for t in time]
control_slope = linregress(x, control)
covered_slope = linregress(x, covered)
print(control_slope[2], covered_slope[2])


def abline(slope, intercept, color, label):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color=color, label=label, alpha=1)


fig, ax = plt.subplots()
plt.xlim(1, 20)
plt.ylim(20, 55)
fontsize = 20
ax.set_xticks(np.arange(2, 22, step=2))
ax.tick_params(labelsize=fontsize)
abline(control_slope[0], control_slope[1], "r", "Control")
abline(covered_slope[0], covered_slope[1], "b", "Covered")
ax.legend(loc="upper left", fontsize=fontsize)
ax.set_xlabel("Time in Seconds ", fontsize=fontsize)
ax.set_ylabel("Temp in C", fontsize=fontsize)
plt.show()
