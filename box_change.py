import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
n=0
control=[]
covered=[]
for file in os.listdir("C:/Users/scott/OneDrive/Desktop/ScienceFair_2024/box"):
    if file.endswith(".csv"):
        n+=1
        data=pd.read_csv(f"C:/Users/scott/OneDrive/Desktop/ScienceFair_2024/box/{file}")
        control_start=(data["Control"].to_list())[0]
        control_end=(data["Control"].to_list())[-1]
        control.append(control_end-control_start)
        covered_start=(data["Salt"].to_list())[0]
        covered_end=(data["Salt"].to_list())[-1]
        covered.append(covered_end-covered_start)
control=np.array(control)
covered=np.array(covered)

avg_control=np.mean(control)
avg_covered=np.mean(covered)

fig, ax =plt.subplots()
fontsize = 12
ax.tick_params(labelsize=fontsize)
ax.bar(
    ["Control", "Covered in\nNaCl Crystals"],
    [avg_control, avg_covered],
    width=0.5,
    color="steelblue",
    align="center",
    alpha=1,
    ecolor="black",
    capsize=10,
)
ax.scatter(["Control"]*len(control), control, c="r")
ax.scatter(["Covered in\nNaCl Crystals"]*len(covered), covered, c="r")
plt.plot([0,1], [control[0], covered[0]], c="r")
plt.plot([0,1], [control[1], covered[1]], c="r")
plt.plot([0,1], [control[2], covered[2]], c="r")
ax.set_ylabel("Temp. Change (C°)", fontsize=fontsize+2)
plt.title("Change in Temp. of Air\nInside Model Structure ")
plt.show()

