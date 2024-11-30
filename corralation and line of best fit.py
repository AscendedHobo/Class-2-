
# Correlation : Ice Cream sales vs Temperature
# 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## get data frame

frame = pd.read_csv("C:/Users/alanw/OneDrive/Documents/GitHub/Class/statsCorrel.csv", header=0, sep=",")
print(frame)


x = frame["Temperature"]
y = frame["Ice_Cream_Sales"]

#frame.plot(x,y , kind="scatter")
frame.plot(x="Temperature", y="Ice_Cream_Sales", kind="scatter")


slope_intercept = np.polyfit(x,y,1)


slope = round(slope_intercept[0])

intercept = round(slope_intercept[1])



print(f'slope :{round(slope_intercept[0])}, intercept : {round(slope_intercept[1])}')
cor = (np.corrcoef(x,y))
print(np.corrcoef(x,y))
cor = np.corrcoef(x, y)[0, 1]  # Extract the correlation coefficient
print(f'Correlation coefficient: {cor:.2f}')

plt.plot(x,(slope*x)+intercept)



plt.show()







# # NB: using cleaned data set
# dataFrame = pd.read_csv("statsCorrel.csv", header=0, sep=",")

# x = dataFrame["Temperature"]
# y = dataFrame["Ice_Cream_Sales"]
# slope_intercept = np.polyfit(x,y,1)
# print(f'slope :{round(slope_intercept[0])}, intercept : {round(slope_intercept[1])}')

# print("Mean x : ", np.mean(x))
# print("Mean y : ", np.mean(y))

# # plot the scatter graph 
# dataFrame.plot(x="Temperature", y="Ice_Cream_Sales", kind="scatter")
# plt.title("Fig 1.0 Ice Creams Sales vs Temperature")
# plt.xlabel("Temperature C")
# plt.ylabel("Ice Cream Sales")
# plt.ylim(ymin=0)    # start from y axis = 0
# plt.xlim(xmin=0)    # start from x axis = 0
# plt.show()          # show the plot
