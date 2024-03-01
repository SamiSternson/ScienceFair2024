# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

# Import data
data1 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/fine1.csv")
data2 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/fine2.csv")
data3 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/fine3.csv")
data4 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/fine4.csv")
data5 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/fine5.csv")
data6 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/fine6.csv")
data1_coarse = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/coarse1.csv")
data2_coarse = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/coarse2.csv")
data3_coarse = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/coarse3.csv")
data4_coarse = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/coarse4.csv")
data5_coarse = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/coarse5.csv")
data6_coarse = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/Copper/coarse6.csv")
# Convert data into list form
coarse1 = data1_coarse["Salt"].tolist()
control1_coarse = data1_coarse["Control"].tolist()
coarse2 = data2_coarse["Salt"].tolist()
control2_coarse = data2_coarse["Control"].tolist()
coarse3 = data3_coarse["Salt"].tolist()
control3_coarse = data3_coarse["Control"].tolist()
coarse4 = data4_coarse["Salt"].tolist()
control4_coarse = data4_coarse["Control"].tolist()
coarse5 = data5_coarse["Salt"].tolist()
control5_coarse = data5_coarse["Control"].tolist()
coarse6 = data6_coarse["Salt"].tolist()
control6_coarse = data6_coarse["Control"].tolist()
fine1 = data1["Salt"].tolist()
control1 = data1["Control"].tolist()
fine2 = data2["Salt"].tolist()
control2 = data2["Control"].tolist()
fine3 = data3["Salt"].tolist()
control3 = data3["Control"].tolist()
fine4 = data4["Salt"].tolist()
control4 = data4["Control"].tolist()
fine5 = data5["Salt"].tolist()
control5 = data5["Control"].tolist()
fine6 = data6["Salt"].tolist()
control6 = data6["Control"].tolist()
time = data1["Time"].tolist()
coarse_control_avg = []
fine_control_avg = []
coarse_avg = []
fine_avg = []
coarse_control_stdm = []
fine_control_stdm = []
coarse_stdm = []
fine_stdm = []
# Calculate Standard Deviation of the Mean
for i in range(len(coarse1)):
    coarse_control = np.array(
        [
            control1_coarse[i],
            control2_coarse[i],
            control3_coarse[i],
            control4_coarse[i],
            control5_coarse[i],
            control6_coarse[i],
        ]
    )
    coarse_control_avg.append(np.mean(coarse_control))
    coarse_control_stdm.append(np.std(coarse_control) / np.sqrt(len(coarse_control)))

    fine_control = np.array(
        [control1[i], control2[i], control3[i], control4[i], control5[i], control6[i]]
    )
    fine_control_avg.append(np.mean(fine_control))
    fine_control_stdm.append((np.std(fine_control)) / (np.sqrt(len(fine_control))))

    coarse = np.array(
        [coarse1[i], coarse2[i], coarse3[i], coarse4[i], coarse5[i], coarse6[i]]
    )
    coarse_avg.append(np.mean(coarse))
    coarse_stdm.append(np.std(coarse) / np.sqrt(len(coarse)))

    fine = np.array([fine1[i], fine2[i], fine3[i], fine4[i], fine5[i], fine6[i]])
    fine_avg.append(np.mean(fine))
    fine_stdm.append(np.std(fine) / np.sqrt(len(fine)))
# Initialize graph settings
fig = plt.figure()
ax1 = fig.add_subplot()
plt.xlim(1, 20)
plt.ylim(20, 80)
fontsize = 16
ax1.set_xticks(np.arange(2, 22, step=2))
ax1.tick_params(labelsize=fontsize)


# Graphs shaded regions between Standard Deviation of the Mean
def graph_between(x, main_y, stdm_up, stdm_down, c, label):
    ax1.plot(x, main_y, c=c, label=label)
    ax1.plot(
        x,
        stdm_up,
        c=c,
        alpha=0.4,
    )
    ax1.plot(
        x,
        stdm_down,
        c=c,
        alpha=0.4,
    )
    ax1.fill_between(
        x,
        stdm_up,
        stdm_down,
        color=c,
        alpha=0.4,
    )


def abline(slope, intercept, color, linestyle):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color=color, alpha=1, linestyle=linestyle)


fine_y = fine1 + fine2 + fine3 + fine4 + fine5 + fine6
control_y = control1 + control2 + control3 + control4 + control5 + control6
coarse_y = coarse1 + coarse2 + coarse3 + coarse4 + coarse5 + coarse6
control_coarse_y = (
    control1_coarse
    + control2_coarse
    + control3_coarse
    + control4_coarse
    + control5_coarse
    + control6_coarse
)
# Calculate linear regressions
fine_regress = linregress(time * 6, fine_y)
fine_slope = fine_regress[0]
control_regress = linregress(time * 6, control_y)
control_slope = control_regress[0]
control_y_int = control_regress[1]
fine_y_int = fine_regress[1]
coarse_regress = linregress(time * 6, coarse_y)
control_coarse_regress = linregress(time * 6, control_coarse_y)
coarse_slope = coarse_regress[0]
control_coarse_slope = control_coarse_regress[0]
control_coarse_y_int = control_coarse_regress[1]
coarse_y_int = coarse_regress[1]

# Graph lines
graph_between(
    time,
    fine_control_avg,
    [point + fine_control_stdm[i] for i, point in enumerate(fine_control_avg)],
    [point - fine_control_stdm[i] for i, point in enumerate(fine_control_avg)],
    "y",
    "Control1",
)
graph_between(
    time,
    coarse_control_avg,
    [point + coarse_control_stdm[i] for i, point in enumerate(coarse_control_avg)],
    [point - coarse_control_stdm[i] for i, point in enumerate(coarse_control_avg)],
    "r",
    "Control2",
)
graph_between(
    time,
    coarse_avg,
    [point + coarse_stdm[i] for i, point in enumerate(coarse_avg)],
    [point - coarse_stdm[i] for i, point in enumerate(coarse_avg)],
    "g",
    "Coarse sea salt",
)
graph_between(
    time,
    fine_avg,
    [point + fine_stdm[i] for i, point in enumerate(fine_avg)],
    [point - fine_stdm[i] for i, point in enumerate(fine_avg)],
    "b",
    "Finely ground crystals",
)
abline(fine_slope, fine_y_int, "b", "--")
abline(coarse_slope, coarse_y_int, "g", "--")
abline(control_slope, control_y_int, "y", "--")
abline(control_coarse_slope, control_coarse_y_int, "r", "--")
# Labels axes
ax1.legend(loc="upper left", fontsize=fontsize - 4)
ax1.set_ylabel("Temp (C°)", fontsize=fontsize)
ax1.set_xlabel("Time in Seconds", fontsize=fontsize)
plt.title(
    "Passive Cooling of Copper Plates by NaCl Crystals",
    fontsize=12,
)
plt.show()
