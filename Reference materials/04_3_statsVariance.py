# Variance - another measure of spread
#
# 1) calc the mean (x-bar) of a column of numbers
# 2) calc : the original value minus x-bar      NB: some values may be negative
# 3) calc : square the differences  ( to get rid of any negative numbers)
# 4) calc : the average of these squared numbers ==> variance
# 5) NB: variance = square of StdDev


import pandas as pd
import numpy as np

# NB: using cleaned up data
healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# Variance of all columns
print(np.var(healthStats))


# Variance of pulse only
Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
print(f"Var of Pulse {np.var(Max_Pulse)}") 

