# read in a CSV file and process using Pandas 

import pandas as pd

# read in the CSV, headers are in row 0, separated by ','s
healthStats = pd.read_csv("data.csv", header=0, sep=",")


print(100 * '-')
print(healthStats)      # print entire table
print(f'Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}')

# drop entire row if it contains NaN values
healthStats.dropna(axis=0, inplace=True) 
print(100 * '-')
print(healthStats)      # print entire table
print(f'Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}')