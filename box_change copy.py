import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
n=0
y=[]
for file in os.listdir("C:/Users/scott/OneDrive/Desktop/ScienceFair_2024/box"):
    if file.endswith(".csv"):
        n+=1
        data=pd.read_csv(f"C:/Users/scott/OneDrive/Desktop/ScienceFair_2024/box/{file}")
        control_start=(data["Control"].to_list())[0]
        control_end=(data["Control"].to_list())[-1]
        control_delta=control_end-control_start
        covered_start=(data["Salt"].to_list())[0]
        covered_end=(data["Salt"].to_list())[-1]
        covered_delta=covered_end-covered_start
        delta_diff=control_delta-covered_delta
        y.append(delta_diff)
avg=np.mean(np.array(y))

fig, ax =plt.subplots()
fontsize = 12
ax.tick_params(labelsize=fontsize)
ax.bar(
    ["Difference in Chang\nin Tempurature"],
    avg,
    width=0.5,
    color="steelblue",
    align="center",
    alpha=1,
    ecolor="black",
    capsize=10,
)
ax.scatter(["Difference in Change\nin Tempurature","Difference in Chang\nin Tempurature"], y, c="r")
ax.set_ylabel("Temp (C°)", fontsize=fontsize+2)
plt.title("Difference Between control and test  in Change\nin Tempurature of Boxes After 2 Hours of Heating")
plt.show()

