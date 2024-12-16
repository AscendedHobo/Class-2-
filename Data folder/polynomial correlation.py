# Import necessary modules
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Polynomial regression (degree = 3)
mymodel = np.poly1d(np.polyfit(x, y, 5))

# Calculate correlation (R-squared score)
r2 = r2_score(y, mymodel(x))
print(f'Correlation (R²): {r2:.4}')

# Generate smooth line for the polynomial curve
myline = np.linspace(1, 22, 100)

# Plot scatter diagram and polynomial regression line
plt.title("Polynomial Correlation")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(myline, mymodel(myline), color='red', label='Polynomial Fit (Degree 3)')
plt.legend()
plt.show()
