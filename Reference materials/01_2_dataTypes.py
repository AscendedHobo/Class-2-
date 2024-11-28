# read in a CSV file and process using Pandas 

import pandas as pd

# read in the CSV, headers are in row 0, separated by ','s
healthStats = pd.read_csv("data.csv", header=0, sep=",")


# drop entire row if it contains NaN values
healthStats.dropna(axis=0, inplace=True) 

# convert avg_pulse and max_pulse to float64 for calcs 
healthStats["Average_Pulse"] = healthStats["Average_Pulse"].astype(float)
healthStats["Max_Pulse"] = healthStats["Max_Pulse"].astype(float)

# print the data and some info
print(100 * '-')
print(healthStats)      # print entire table
print(f'Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}')
print(healthStats.info())      # print data types
print(healthStats.describe())  # analyse the data 

