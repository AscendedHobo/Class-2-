# plot a line from incoming data

import pandas as pd
import numpy as np

# import data from csv file
healthStats = pd.read_csv("data.csv", header=0, sep=",")

# drop entire row if it contains NaN values
healthStats.dropna(axis=0, inplace=True) 

x = healthStats["Average_Pulse"]
y = healthStats["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)

print(f'slope :{round(slope_intercept[0])}, intercept : {round(slope_intercept[1])}')
