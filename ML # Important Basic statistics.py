# import necessary modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
 
 
 
# set up mydata
#myData = [45,34,54,34,67,78,89,67,56,34, 65,45,34,54,45,56,56,56,43,23,56,45,65,45]
 
myData = np.random.normal(0, 100, 10000)     # (lowest-value, highest-value, number of numbers)
 
#myData.sort()
#print(myData)
 
# Important Basic statistics
print(f'Mean   :\t {np.mean(myData):.5}')
print(f'Median :\t {np.median(myData):.5}')
print(f'Mode   : \t{st.mode(myData)}')
print(f'StdDev :\t {np.std(myData):.5}')
print(f'Var    :\t {np.var(myData):.5}')
print(f'25th % :\t {np.percentile(myData, 25):.3}')
print(f'75th % :\t {np.percentile(myData, 75):.3}')

 
 
plt.hist(myData, 10)        # 10 columns of data in my histogram
plt.show()


myData = np.random.normal(0, 100, 10000)     # (lowest-value, highest-value, number of numbers)
 
#myData.sort()
#print(myData)
 
# Important Basic statistics
print(f'Mean   :\t {np.mean(myData):.5}')
print(f'Median :\t {np.median(myData):.5}')
print(f'Mode   : \t{st.mode(myData)}')
print(f'StdDev :\t {np.std(myData):.5}')
print(f'Var    :\t {np.var(myData):.5}')
print(f'25th % :\t {np.percentile(myData, 25):.3}')
print(f'75th % :\t {np.percentile(myData, 75):.3}')

 
 
plt.hist(myData, 10)        # 10 columns of data in my histogram
plt.show()
