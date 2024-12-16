#############################################################################################################################

# ▪ Measures of Central Tendency : mean, median, mode
# # Import necessary modules
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats as st

# # Data
# myData = [45, 34, 54, 34, 67, 78, 89, 67, 56, 34, 65, 45, 34, 54, 45, 56, 56, 56, 43, 23, 56, 45, 65, 45]

# # Important Basic Statistics
# print(f'Mean:    {np.mean(myData):.5}')
# print(f'Median:  {np.median(myData):.5}')
# print(f'Mode:    {st.mode(myData)}')

# # Histogram with 10 bins
# plt.hist(myData, bins=10)
# plt.title("Histogram of myData")
# plt.xlabel("Value Range")
# plt.ylabel("Frequency")
# plt.show()

#########################################################################################################################
# # ▪ Measures of Dispersion (from the mean)
# # Import necessary modules
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats as st

# # Set up myData
# myData = [45, 34, 54, 34, 67, 78, 89, 67, 56, 34, 65, 45, 34, 54, 45, 56, 56, 56, 43, 23, 56, 45, 65, 45]

# # Statistics
# print(f'StdDev:   {np.std(myData):.5}')
# print(f'Variance: {np.var(myData):.5}')
# print(f'25th %:   {np.percentile(myData, 25):.5}')
# print(f'75th %:   {np.percentile(myData, 75):.5}')

# # Histogram with 10 bins
# plt.hist(myData, bins=10, color='skyblue', edgecolor='black')
# plt.title("Histogram of myData")
# plt.xlabel("Value Range")
# plt.ylabel("Frequency")
# plt.show()

######################################################################################################################################

# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

# Generate a dataset of random floats with mean=5 and stdDev=1
myData = np.random.normal(5.0, 1.0, 100000)  # mean, stdDev, N

# Statistics
print(f'Mean:     {np.mean(myData):.5}')
print(f'Median:   {np.median(myData):.5}')
print(f'Mode:     {st.mode(myData)}')
print(f'StdDev:   {np.std(myData):.5}')
print(f'25th %:   {np.percentile(myData, 25):.5}')
print(f'75th %:   {np.percentile(myData, 75):.5}')

# Plot a histogram with 1000 bins
plt.title("Normal Distribution with Mean = 5, StdDev = 1")
plt.xlabel("Random Numbers")
plt.ylabel("Frequency")
plt.hist(myData, bins=1000, color='skyblue', edgecolor='black')
plt.show()

