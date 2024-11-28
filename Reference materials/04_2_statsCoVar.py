# CoVar - Coefficint of Variance 
# 
# measure of how large the StdDev is...
# 
# CoVar = stdDev / mean


import pandas as pd
import numpy as np

# NB: using cleaned up data
healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# CoVar of all columns
print(np.std(healthStats)/np.mean(healthStats) )


# CoVar of pulse only
Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
print(f"Std  of Pulse {np.std(Max_Pulse)}") 
print(f"Mean of Pulse {np.mean(Max_Pulse)}") 
print(f"CoVar of Pulse (std / mean ) {np.std(Max_Pulse) / np.mean(Max_Pulse) }") 

