import pandas as pd
import numpy as np
 
health_data = pd.read_csv("C:/Users/alanw/Documents/GitHub/Class/Lesson27/11/data.csv", header=0, sep=",")
 
x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)
 
print(f'slope :{round(slope_intercept[0])}, intercept : {round(slope_intercept[1])}')
 