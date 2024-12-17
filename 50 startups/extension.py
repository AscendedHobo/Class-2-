# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D

# Read the data
df = pd.read_csv(r"C:\Users\alanw\Documents\GitHub\Class\50 startups\50_Startups.csv")

# Separate the data by states
ny_data = df[df['State'] == 'New York']
ca_data = df[df['State'] == 'California']
fl_data = df[df['State'] == 'Florida']

# Normalize the data (scale to range [0, 1])
scaler = MinMaxScaler()

# Apply MinMaxScaler to 'R&D Spend', 'Marketing Spend', and 'Profit' for all states
df[['R&D Spend', 'Marketing Spend', 'Profit']] = scaler.fit_transform(df[['R&D Spend', 'Marketing Spend', 'Profit']])

# Apply MinMaxScaler to each state data separately
ny_data[['R&D Spend', 'Marketing Spend', 'Profit']] = scaler.fit_transform(ny_data[['R&D Spend', 'Marketing Spend', 'Profit']])
ca_data[['R&D Spend', 'Marketing Spend', 'Profit']] = scaler.fit_transform(ca_data[['R&D Spend', 'Marketing Spend', 'Profit']])
fl_data[['R&D Spend', 'Marketing Spend', 'Profit']] = scaler.fit_transform(fl_data[['R&D Spend', 'Marketing Spend', 'Profit']])

# Prepare the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a function to plot the 3D plane
def plot_plane(data, ax, label, color):
    X = data[['R&D Spend', 'Marketing Spend']]  # Use R&D Spend and Marketing Spend for X axis
    y = data['Profit']  # Profit for Z axis
    model = LinearRegression()  # Linear regression model
    model.fit(X, y)  # Fit the model to the data

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
ax.set_title('3D Plane of Best Fit for Profit vs R&D Spend and Marketing Spend (Normalized)')

# Show the plot with legend
plt.legend()
plt.show()

# Print correlation coefficients per state
ny_rnd_corr = ny_data[['R&D Spend', 'Profit']].corr().iloc[0, 1]
ny_marketing_corr = ny_data[['Marketing Spend', 'Profit']].corr().iloc[0, 1]

ca_rnd_corr = ca_data[['R&D Spend', 'Profit']].corr().iloc[0, 1]
ca_marketing_corr = ca_data[['Marketing Spend', 'Profit']].corr().iloc[0, 1]

fl_rnd_corr = fl_data[['R&D Spend', 'Profit']].corr().iloc[0, 1]
fl_marketing_corr = fl_data[['Marketing Spend', 'Profit']].corr().iloc[0, 1]

print(f"New York:\nR&D Spend vs Profit Correlation = {ny_rnd_corr}\nMarketing Spend vs Profit Correlation = {ny_marketing_corr}")
print(f"\nCalifornia:\nR&D Spend vs Profit Correlation = {ca_rnd_corr}\nMarketing Spend vs Profit Correlation = {ca_marketing_corr}")
print(f"\nFlorida:\nR&D Spend vs Profit Correlation = {fl_rnd_corr}\nMarketing Spend vs Profit Correlation = {fl_marketing_corr}")
