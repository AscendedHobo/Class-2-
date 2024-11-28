# 
# Corelation measures how closely two variables are related
# 
# it is a number between +1 and -1
#   +1 : the two variables are positively related
#    0 : the two variables are not related 
#   +1 : the two variables are negatively related# 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# NB: using cleaned data set
healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# plot the scatter graph of Duration and Pulse
healthStats.plot(x ='Duration', y='Max_Pulse', kind='scatter')
plt.title("Fig 1.0 Duration vs Pulse")
plt.xlabel("Duration")
plt.ylabel("Pulse")
plt.ylim(ymin=0)    # start from y axis = 0
plt.xlim(xmin=0)    # start from x axis = 0
plt.show()          # show the plot

