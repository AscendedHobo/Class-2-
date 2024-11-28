# Program to show charts using MathPlotLIb
 
# Import numpy, etc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# load data file
healthStats = pd.read_csv("C:/Users/alanw/Documents/GitHub/Class/Lesson27/11/data.csv", header=0, sep=",")
 
# clean the data for processing
healthStats.dropna(axis=0, inplace=True)        # drop any non numerivc data rows
 
# print basic stats
print(healthStats.describe())
 
# produce charts & diagrams
healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="scatter")
 
# display the chart
plt.title("This is the Title")
plt.ylabel("Y title")
plt.xlabel("X title")
plt.ylim(0)
plt.xlim(0)
plt.show()          # show the plot
 
 
 
 