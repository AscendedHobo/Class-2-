import pandas as pd
import numpy as np

# NB: using cleaned up data
healthStats = pd.read_csv("data2.csv", header=0, sep=",")

# describe the basics stats 
print(healthStats.describe())

# 10% percentile means that 10% of items are below the 10th percentile
Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
percent10 = np.percentile(Max_Pulse, 10)    # we want the 10th percentile
print(f"10th percentile : {percent10}") 

