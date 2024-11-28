# # using Python min max functions

# age = [23,45,32,45,32,54,64,45,34]

# print(f'Min Age  : {min(age)}')
# print(f'Max Age  : {max(age)}')

# import numpy as np

# # using NumPy functions 

# age = [23,45,32,45,32,54,64,45,34]

# print(f'Mean Average : {np.mean(age)}')

# # read in a CSV file and process using Pandas 

# import pandas as pd

# # read in the CSV, headers are in row 0, separated by ','s
# healthStats = pd.read_csv("data.csv", header=0, sep=",")

# print(100 * '-')
# print(healthStats.head())   # print top 5 rows


# print(100 * '-')
# print(healthStats)      # print entire table

# # read in a CSV file and process using Pandas 

# import pandas as pd

# # read in the CSV, headers are in row 0, separated by ','s
# healthStats = pd.read_csv("data.csv", header=0, sep=",")


# print(100 * '-')
# print(healthStats)      # print entire table
# print(f'Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}')

# # drop entire row if it contains NaN values
# healthStats.dropna(axis=0, inplace=True) 
# print(100 * '-')
# print(healthStats)      # print entire table
# print(f'Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}')
# #

# # read in a CSV file and process using Pandas 

# import pandas as pd

# # read in the CSV, headers are in row 0, separated by ','s
# healthStats = pd.read_csv("data.csv", header=0, sep=",")


# # drop entire row if it contains NaN values
# healthStats.dropna(axis=0, inplace=True) 

# # convert avg_pulse and max_pulse to float64 for calcs 
# healthStats["Average_Pulse"] = healthStats["Average_Pulse"].astype(float)
# healthStats["Max_Pulse"] = healthStats["Max_Pulse"].astype(float)

# # print the data and some info
# print(100 * '-')
# print(healthStats)      # print entire table
# print(f'Rows: {healthStats.shape[0]}, columns : {healthStats.shape[1]}')
# print(healthStats.info())      # print data types
# print(healthStats.describe())  # analyse the data 

# # plot a line from incoming data

# import pandas as pd
# import matplotlib.pyplot as plt

# # import data from csv file
# healthStats = pd.read_csv("data.csv", header=0, sep=",")

# # drop entire row if it contains NaN values
# healthStats.dropna(axis=0, inplace=True) 

# # healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="line")
# healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="bar")
# # healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="scatter")
# # healthStats.plot(x="Average_Pulse", y="Calorie_Burnage", kind="pie")

# plt.title("Fig 1.0 Average Pulse vs Calories Burned")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calories Burned")
# plt.ylim(ymin=0)    # start from y axis = 0
# plt.xlim(xmin=0)    # start from x axis = 0
# plt.show()          # show the plot

# import pandas as pd
# import numpy as np

# health_data = pd.read_csv("data2.csv", header=0, sep=",")

# x = health_data["Average_Pulse"]
# y = health_data["Calorie_Burnage"]
# slope_intercept = np.polyfit(x,y,1)

# print(f'slope :{round(slope_intercept[0])}, intercept : {round(slope_intercept[1])}')

# # plot a line from incoming data

# import pandas as pd
# import numpy as np

# # import data from csv file
# healthStats = pd.read_csv("data.csv", header=0, sep=",")

# # drop entire row if it contains NaN values
# healthStats.dropna(axis=0, inplace=True) 

# x = healthStats["Average_Pulse"]
# y = healthStats["Calorie_Burnage"]
# slope_intercept = np.polyfit(x,y,1)

# print(f'slope :{round(slope_intercept[0])}, intercept : {round(slope_intercept[1])}')

# import pandas as pd
# import numpy as np

# # NB: using cleaned up data
# healthStats = pd.read_csv("data2.csv", header=0, sep=",")

# # describe the basics stats 
# print(healthStats.describe())

# # 10% percentile means that 10% of items are below the 10th percentile
# Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
# percent10 = np.percentile(Max_Pulse, 10)    # we want the 10th percentile
# print(f"10th percentile : {percent10}") 

# # STD Dev defines how spread the data observations is
# # a low stddev means values are close to the mean
# # a high stddev means values are spread out over a range
# #
# # trying to predict a value accuratly will depend on the spread of data, i.e stddev


# import pandas as pd
# import numpy as np

# # NB: using cleaned up data
# healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# # stdDev of all columns
# print(np.std(healthStats))

# # stdDev of pulse only
# Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
# stdDev = np.std(Max_Pulse) 
# print(f"Pulse stdDev : {stdDev}") 

# # CoVar - Coefficint of Variance 
# # 
# # measure of how large the StdDev is...
# # 
# # CoVar = stdDev / mean


# import pandas as pd
# import numpy as np

# # NB: using cleaned up data
# healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# # CoVar of all columns
# print(np.std(healthStats)/np.mean(healthStats) )


# # CoVar of pulse only
# Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
# print(f"Std  of Pulse {np.std(Max_Pulse)}") 
# print(f"Mean of Pulse {np.mean(Max_Pulse)}") 
# print(f"CoVar of Pulse (std / mean ) {np.std(Max_Pulse) / np.mean(Max_Pulse) }") 

# # Variance - another measure of spread
# #
# # 1) calc the mean (x-bar) of a column of numbers
# # 2) calc : the original value minus x-bar      NB: some values may be negative
# # 3) calc : square the differences  ( to get rid of any negative numbers)
# # 4) calc : the average of these squared numbers ==> variance
# # 5) NB: variance = square of StdDev


# import pandas as pd
# import numpy as np

# # NB: using cleaned up data
# healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# # Variance of all columns
# print(np.var(healthStats))


# # Variance of pulse only
# Max_Pulse = healthStats["Max_Pulse"]        # isolate the Max Pulse data
# print(f"Var of Pulse {np.var(Max_Pulse)}") 

# # 
# # Corelation measures how closely two variables are related
# # 
# # it is a number between +1 and -1
# #   +1 : the two variables are positively related
# #    0 : the two variables are not related 
# #   +1 : the two variables are negatively related# 

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # NB: using cleaned data set
# healthStats = pd.read_csv("data2.csv", header=0, sep=",")

# # plot the scatter graph of Pulse and Calories
# healthStats.plot(x="Duration", y="Calorie_Burnage", kind="scatter")
# plt.title("Fig 1.0 Average Pulse vs Calories Burned")
# plt.xlabel("Duration")
# plt.ylabel("Calories Burned")
# plt.ylim(ymin=0)    # start from y axis = 0
# plt.xlim(xmin=0)    # start from x axis = 0
# plt.show()          # show the plot

# # 
# # Corelation measures how closely two variables are related
# # 
# # it is a number between +1 and -1
# #   +1 : the two variables are positively related
# #    0 : the two variables are not related 
# #   +1 : the two variables are negatively related# 

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # NB: using cleaned data set
# healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# # plot the scatter graph of Duration and Pulse
# healthStats.plot(x ='Duration', y='Max_Pulse', kind='scatter')
# plt.title("Fig 1.0 Duration vs Pulse")
# plt.xlabel("Duration")
# plt.ylabel("Pulse")
# plt.ylim(ymin=0)    # start from y axis = 0
# plt.xlim(xmin=0)    # start from x axis = 0
# plt.show()          # show the plot

# # 
# # Corelation Matrix shows correlation between all columns

# import pandas as pd

# # NB: using full data set
# healthStats = pd.read_csv("fullData.csv", header=0, sep=",")

# # show the full correlation matrix
# print(round(healthStats.corr(),2))

# # 
# # Corelation Matrix shown as a heat map
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# healthStats = pd.read_csv("fullData.csv", header=0, sep=",")
# correlation_full_health = healthStats.corr()

# axis_corr = sns.heatmap(correlation_full_health,vmin=-1, vmax=1,center=0,
#                         cmap=sns.diverging_palette(50, 500, n=500),
#                         square=True)

# plt.show()


# #
# # Causality : one thing causes another
# # 
# # Just because correlation may be +/-1 does not mean one thing implies the other
# # 
# # example from W3Schools
# # https://www.w3schools.com/datascience/ds_stat_correlation_causality.asp
# #  

# import pandas as pd
# import matplotlib.pyplot as plt

# Drowning_Accident = [20,40,60,80,100,120,140,160,180,200]
# Ice_Cream_Sale = [20,40,60,80,100,120,140,160,180,200]

# Drowning = {"Drowning_Accident": [20,40,60,80,100,120,140,160,180,200],
# "Ice_Cream_Sale": [20,40,60,80,100,120,140,160,180,200]}

# Drowning = pd.DataFrame(data=Drowning)

# Drowning.plot(x="Ice_Cream_Sale", y="Drowning_Accident", kind="scatter")
# plt.show()

# correlation_beach = Drowning.corr()
# print(correlation_beach)
