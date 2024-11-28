#
# Causality : one thing causes another
# 
# Just because correlation may be +/-1 does not mean one thing implies the other
# 
# example from W3Schools
# https://www.w3schools.com/datascience/ds_stat_correlation_causality.asp
#  

import pandas as pd
import matplotlib.pyplot as plt

Drowning_Accident = [20,40,60,80,100,120,140,160,180,200]
Ice_Cream_Sale = [20,40,60,80,100,120,140,160,180,200]

Drowning = {"Drowning_Accident": [20,40,60,80,100,120,140,160,180,200],
"Ice_Cream_Sale": [20,40,60,80,100,120,140,160,180,200]}

Drowning = pd.DataFrame(data=Drowning)

Drowning.plot(x="Ice_Cream_Sale", y="Drowning_Accident", kind="scatter")
plt.show()

correlation_beach = Drowning.corr()
print(correlation_beach)
