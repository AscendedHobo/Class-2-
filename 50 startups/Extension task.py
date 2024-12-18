# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv(r"C:\Users\alanw\OneDrive\Documents\GitHub\Class\50 startups\50_Startups.csv")

# Separate the data by states
ny_data = df[df['State'] == 'New York']
ca_data = df[df['State'] == 'California']
fl_data = df[df['State'] == 'Florida']



# Define a function to run linear regression and get coefficients
def get_coefficients(data, feature_column, target_column):
    X = data[[feature_column]]
    y = data[target_column]
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_[0]  # Returning the coefficient of the feature

# Get coefficients for each state
ny_rnd_coef = get_coefficients(ny_data, 'R&D Spend', 'Profit')
ny_marketing_coef = get_coefficients(ny_data, 'Marketing Spend', 'Profit')

ca_rnd_coef = get_coefficients(ca_data, 'R&D Spend', 'Profit')
ca_marketing_coef = get_coefficients(ca_data, 'Marketing Spend', 'Profit')

fl_rnd_coef = get_coefficients(fl_data, 'R&D Spend', 'Profit')
fl_marketing_coef = get_coefficients(fl_data, 'Marketing Spend', 'Profit')

print(f"New York: R&D Coefficient = {ny_rnd_coef}, Marketing Coefficient = {ny_marketing_coef}")
print(f"California: R&D Coefficient = {ca_rnd_coef}, Marketing Coefficient = {ca_marketing_coef}")
print(f"Florida: R&D Coefficient = {fl_rnd_coef}, Marketing Coefficient = {fl_marketing_coef}")


# Prepare the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a function to plot the plane
def plot_plane(data, ax, label, color):
    X = data[['R&D Spend', 'Marketing Spend']]
    y = data['Profit']
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate a grid of values for R&D Spend and Marketing Spend
    x_range = np.linspace(X['R&D Spend'].min(), X['R&D Spend'].max(), 10)
    y_range = np.linspace(X['Marketing Spend'].min(), X['Marketing Spend'].max(), 10)
    x_grid, y_grid = np.meshgrid(x_range, y_range)
    z_grid = model.predict(np.c_[x_grid.ravel(), y_grid.ravel()]).reshape(x_grid.shape)
    
    # Plot the plane
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5, color=color)
    ax.scatter(X['R&D Spend'], X['Marketing Spend'], y, color=color, label=label)

# Plot for New York
plot_plane(ny_data, ax, 'New York', 'r')

# Plot for California
plot_plane(ca_data, ax, 'California', 'g')

# Plot for Florida
plot_plane(fl_data, ax, 'Florida', 'b')

# Label the plot
ax.set_xlabel('R&D Spend')
ax.set_ylabel('Marketing Spend')
ax.set_zlabel('Profit')
ax.set_title('3D Plane of Best Fit for Profit vs R&D Spend and Marketing Spend')

# Show the plot
plt.legend()
plt.show()


# Importing necessary libraries
from sklearn.linear_model import LinearRegression

# Define a function to run linear regression and get the coefficient
def get_coefficients(data, feature_column, target_column):
    X = data[[feature_column]]  # Features matrix (2D array)
    y = data[target_column]     # Target variable (1D array)
    model = LinearRegression()  # Linear regression model
    model.fit(X, y)             # Fit the model to the data
    return model.coef_[0]       # Return the coefficient (slope of the feature)

# Get the coefficient for Marketing Spend vs Profit for the entire dataset
marketing_coef = get_coefficients(df, 'Marketing Spend', 'Profit')

# Output the result
print(f"Marketing Spend vs Profit Coefficient = {marketing_coef}")

print(df[['Marketing Spend', 'Profit']].describe())


# # Coefficient for profit per spend of x for each state + pretty if useless graph
# New York: R&D Coefficient = 0.8131794658029954, Marketing Coefficient = 0.22186556576949426
# California: R&D Coefficient = 0.9284303973517376, Marketing Coefficient = 0.3045593013838519
# Florida: R&D Coefficient = 0.8133551243584262, Marketing Coefficient = 0.22541029749435051

