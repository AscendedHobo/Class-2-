# read in a CSV file and process using Pandas 

import pandas as pd

# read in the CSV, headers are in row 0, separated by ','s
healthStats = pd.read_csv("data.csv", header=0, sep=",")

print(100 * '-')
print(healthStats.head())   # print top 5 rows


print(100 * '-')
print(healthStats)      # print entire table
