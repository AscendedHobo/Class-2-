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



# Load the dataset
df = pd.read_csv(r"C:\Users\alanw\Documents\GitHub\Class\50 startups\50_Startups.csv")





#####################################################################################################

# Display first few rows
print(df.head())

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Check for duplicates
print("Duplicate Rows:", df.duplicated().sum())

# Check data types
print("Data Types:\n", df.dtypes)

# Basic summary statistics
print("Summary Statistics:\n", df.describe())

#####################################################################################################


#drop the states for calulations
# Drop non-numeric columns
df_numeric = df.select_dtypes(include=[np.number])

# Calculate correlation matrix
correlation_matrix = df_numeric.corr()

# Display correlation matrix
print("Correlation Matrix:\n", correlation_matrix)

# Visualize the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()

# #####################################################################################################

# # Calculate correlation coefficients
# corr_rd = df['R&D Spend'].corr(df['Profit'])
# corr_admin = df['Administration'].corr(df['Profit'])
# corr_marketing = df['Marketing Spend'].corr(df['Profit'])

# # Scatter Plots for Profit vs Expenditures with Lines of Best Fit
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# # R&D Spend
# sns.regplot(x='R&D Spend', y='Profit', data=df, ax=axes[0], scatter_kws={"color": "blue"}, line_kws={"color": "red"})
# axes[0].set_title(f"R&D Spend vs Profit\nCorrelation: {corr_rd:.2f}")

# # Administration
# sns.regplot(x='Administration', y='Profit', data=df, ax=axes[1], scatter_kws={"color": "green"}, line_kws={"color": "red"})
# axes[1].set_title(f"Administration vs Profit\nCorrelation: {corr_admin:.2f}")

# # Marketing Spend
# sns.regplot(x='Marketing Spend', y='Profit', data=df, ax=axes[2], scatter_kws={"color": "purple"}, line_kws={"color": "red"})
# axes[2].set_title(f"Marketing Spend vs Profit\nCorrelation: {corr_marketing:.2f}")

# plt.tight_layout()
# plt.show()




# #####################################################################################################

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.preprocessing import PolynomialFeatures

# # Prepare the data
# X = df[['R&D Spend', 'Marketing Spend']]  # Two most correlated features
# y = df['Profit']

# # 1. Fit a Multiple Linear Regression Model
# model = LinearRegression()
# model.fit(X, y)

# # Predictions
# y_pred = model.predict(X)

# # Model performance
# r2 = r2_score(y, y_pred)
# print(f"R^2 Score for Multi-Variable Linear Regression: {r2:.2f}")

# # 2. 3D Scatter Plot with Regression Plane
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111, projection='3d')

# # Scatter Plot of Actual Data
# ax.scatter(df['R&D Spend'], df['Marketing Spend'], df['Profit'], color='blue', label='Actual Data')

# # Create a Mesh Grid for the Regression Plane
# rnd_spend = np.linspace(df['R&D Spend'].min(), df['R&D Spend'].max(), 20)
# marketing_spend = np.linspace(df['Marketing Spend'].min(), df['Marketing Spend'].max(), 20)
# rnd_spend, marketing_spend = np.meshgrid(rnd_spend, marketing_spend)
# profit_plane = model.intercept_ + model.coef_[0] * rnd_spend + model.coef_[1] * marketing_spend

# # Plot the Regression Plane
# ax.plot_surface(rnd_spend, marketing_spend, profit_plane, color='red', alpha=0.5)

# # Labels and Title
# ax.set_xlabel('R&D Spend')
# ax.set_ylabel('Marketing Spend')
# ax.set_zlabel('Profit')
# ax.set_title('Multi-Variable Linear Regression: R&D Spend and Marketing Spend vs Profit')
# plt.legend()
# plt.show()



#####################################################################################################


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures

# Prepare the data
X = df[['R&D Spend', 'Marketing Spend']]  # Two most correlated features
y = df['Profit']

# 1. Fit a Multiple Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Model performance
r2 = r2_score(y, y_pred)

# Print the results
print("Multiple Linear Regression Analysis:")
print(f"R^2 Score for the model: {r2:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficients for R&D Spend and Marketing Spend: {model.coef_}")

# Print predictions for the first few rows
print("\nPredicted Profit for the first few records:")
for i in range(5):
    print(f"R&D Spend = {df['R&D Spend'].iloc[i]:.2f}, Marketing Spend = {df['Marketing Spend'].iloc[i]:.2f} => Predicted Profit = {y_pred[i]:.2f}")

# 2. 3D Scatter Plot with Regression Plane
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter Plot of Actual Data
ax.scatter(df['R&D Spend'], df['Marketing Spend'], df['Profit'], color='blue', label='Actual Data')

# Create a Mesh Grid for the Regression Plane
rnd_spend = np.linspace(df['R&D Spend'].min(), df['R&D Spend'].max(), 20)
marketing_spend = np.linspace(df['Marketing Spend'].min(), df['Marketing Spend'].max(), 20)
rnd_spend, marketing_spend = np.meshgrid(rnd_spend, marketing_spend)
profit_plane = model.intercept_ + model.coef_[0] * rnd_spend + model.coef_[1] * marketing_spend

# Plot the Regression Plane
ax.plot_surface(rnd_spend, marketing_spend, profit_plane, color='red', alpha=0.5)

# Labels and Title
ax.set_xlabel('R&D Spend')
ax.set_ylabel('Marketing Spend')
ax.set_zlabel('Profit')
ax.set_title('Multi-Variable Linear Regression: R&D Spend and Marketing Spend vs Profit')

# Show the plot
plt.legend()
plt.show()
