import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#######################################################################################################################################
# import csv as dataframe
dataframe = pd.read_csv("worldPopulation.csv")

# formating data for sorting later
# needed because the population is currently a string, and needs to be int for sort and commas need replacing...
dataframe['value'] = dataframe['value'].str.replace(",", "").astype(int)

#Create pandas array of rows with ranking < 6 
topFive = dataframe[dataframe['ranking'] < 6]

#sorting data by population
topFive = topFive.sort_values(by="value")


#ploting by headers in those rows name is x value is y
plt.bar(topFive["name"] , topFive["value"] )



#Labels and titles
plt.ylabel("Population")
plt.xlabel("Country")
plt.title("Population by Country")

# Showing
plt.show()
#######################################################################################################################################