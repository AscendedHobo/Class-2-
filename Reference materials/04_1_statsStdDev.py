# STD Dev defines how spread the data observations is
# a low stddev means values are close to the mean
# a high stddev means values are spread out over a range
#
# trying to predict a value accuratly will depend on the spread of data, i.e stddev


import pandas as pd
import numpy as np

# NB: using cleaned up data
healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# stdDev of all columns
print(np.std(healthStats))

# stdDev of pulse only
Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
stdDev = np.std(Max_Pulse) 
print(f"Pulse stdDev : {stdDev}") 

