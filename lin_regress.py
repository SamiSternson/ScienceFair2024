import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

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
x = time * 6
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
fine_regress = linregress(x, fine_y)
fine_slope = fine_regress[0]
control_regress = linregress(x, control_y)
control_slope = control_regress[0]
control_y_int = control_regress[1]
fine_y_int = fine_regress[1]
coarse_regress = linregress(x, coarse_y)
control_coarse_regress = linregress(x, control_coarse_y)
coarse_slope = coarse_regress[0]
control_coarse_slope = control_coarse_regress[0]
control_coarse_y_int = control_coarse_regress[1]
coarse_y_int = coarse_regress[1]
print(control_regress[2])
print(control_coarse_regress[2])
print(fine_regress[2])
print(coarse_regress[2])


def abline(slope, intercept, color, label):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color=color, label=label, alpha=1)


fig = plt.figure()
ax1 = fig.add_subplot()
plt.xlim(0, 20)
plt.ylim(20, 80)
fontsize = 18
ax1.set_xticks(np.arange(2, 22, step=2))
ax1.tick_params(labelsize=fontsize)
# Graph Lines
abline(
    control_coarse_slope,
    control_coarse_y_int,
    "b",
    label="Coarse Sea Salt Control",
)
abline(control_slope, control_y_int, "g", label="Fine Control")
abline(
    coarse_slope,
    coarse_y_int,
    "y",
    label="Coarse Sea Salt",
)
abline(
    fine_slope,
    fine_y_int,
    "r",
    label="Fine",
)

# Graph standard deviation of the mean
plt.fill()
ax1.legend(loc="upper left", fontsize=fontsize)
ax1.set_ylabel("Temp C", fontsize=fontsize)
ax1.set_xlabel("Time in Seconds", fontsize=fontsize)
plt.show()
