# 
# Corelation Matrix shows correlation between all columns

import pandas as pd

# NB: using full data set
healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# show the full correlation matrix
print(round(healthStats.corr(),2))
