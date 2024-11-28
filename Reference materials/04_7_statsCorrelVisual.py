# 
# Corelation Matrix shown as a heat map
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

healthStats = pd.read_csv("fullData.csv", header=0, sep=",")
correlation_full_health = healthStats.corr()

axis_corr = sns.heatmap(correlation_full_health,vmin=-1, vmax=1,center=0,
                        cmap=sns.diverging_palette(50, 500, n=500),
                        square=True)

plt.show()
