
# read in a CSV file and process using Pandas
import pandas as pd
# load the CSV, headers are in row 0, separated by ',’s
healthStats = pd.read_csv("C:/Users/alanw/Documents/GitHub/Class/Lesson27/11/data.csv", header=0, sep=",")
print(100 * '-')

print(100 * '-')
healthStats.dropna(axis=0, inplace=True) 
healthStats["Average_Pulse"] = healthStats["Average_Pulse"].astype(float)
healthStats["Max_Pulse"] = healthStats["Max_Pulse"].astype(float)

# print the data and some info
print(100 * '-')
print(healthStats)
print(f"Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}")
print(healthStats.info()) # print data types

print(healthStats.describe()) # analyse the data 
