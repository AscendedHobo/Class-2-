# plot a line from incoming data

import pandas as pd
import matplotlib.pyplot as plt

# import data from csv file
healthStats = pd.read_csv("data.csv", header=0, sep=",")

# drop entire row if it contains NaN values
healthStats.dropna(axis=0, inplace=True) 

# healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="line")
healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="bar")
# healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="scatter")
# healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="pie")

plt.title("Fig 1.0 Average Pulse vs Calories Burned")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burned")
plt.ylim(ymin=0)    # start from y axis = 0
plt.xlim(xmin=0)    # start from x axis = 0
plt.show()          # show the plot

