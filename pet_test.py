import csv
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data1 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/moving1.csv")
data2 = pd.read_csv("C:/Users/scott/Desktop/ScienceFair_2024/packets/moving2.csv")
time = data1["Time"].tolist()
sensor1_1 = data1["Sensor1"].tolist()
sensor2_1 = data1["Sensor2"].tolist()
sensor1_2 = data2["Sensor1"].tolist()
sensor2_2 = data2["Sensor2"].tolist()
sensor1_1_slope = linregress(time, sensor1_1)
sensor2_1_slope = linregress(time, sensor2_1)
sensor1_2_slope = linregress(time, sensor1_2)
sensor2_2_slope = linregress(time, sensor2_2)
print(sensor1_1_slope[0], sensor1_2_slope[0])
print(sensor2_1_slope[0], sensor2_2_slope[0])
fig, ax = plt.subplots()
ax.plot(time, sensor1_1, c="r", label="Sensor1")
ax.plot(time, sensor2_1, c="r", label="Sensor2", linestyle="dotted")
ax.plot(time, sensor1_2, c="b", label="Sensor1")
ax.plot(time, sensor2_2, c="b", label="Sensor2", linestyle="dotted")
ax.legend(loc="upper left")
ax.set_xlabel("Time")
ax.set_ylabel("Temp in C")
plt.show()
