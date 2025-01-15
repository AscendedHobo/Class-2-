# Import necessary modules
import pandas
from sklearn.linear_model import LinearRegression

# Load the data
df = pandas.read_csv(r"C:\Users\alanw\OneDrive\Documents\GitHub\Class\Data folder\carData.csv")

# Define independent variables (Weight, Volume) and dependent variable (CO2)
X = df[['Weight', 'Volume']]
y = df['CO2']

# Create and train the regression model
regr = LinearRegression()
regr.fit(X, y)

# Predict the CO2 emission for a specific car
predictedCO2 = regr.predict([[2300, 1300]])
print(f"Predicted CO2 emission: {predictedCO2[0]:.2f}")


# # Multi variable regression
# import pandas
# from sklearn import linear_model
# df = pandas.read_csv(r"C:\Users\alanw\OneDrive\Documents\GitHub\Class\Data folder\carData.csv")

# X = df[['Weight', 'Volume']]
# y = df['CO2']
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
# #predict the CO2 emission of a car where the weight=2300g, and vol= 1300ccm:
# predictedCO2 = regr.predict([[2300, 1300]])
# print(predictedCO2)
