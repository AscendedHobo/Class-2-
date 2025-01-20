import numpy as np 
import matplotlib.pyplot as plt

months =  ["April","May", "June" , "July", "August", "September", "October" , "November" , "December", "January" , "February" , "March"]

sales = [20078, 20287 , 19982 , 20271 , 20184 , 20265 , 20314 , 20373 , 20168, 20371 , 20207 , 19897 ,]

plt.figure(figsize=(15,20))
plt.bar(months,sales)
plt.ylim(19500, max(sales))
plt.ylabel("Sales")
plt.xlabel("Months")
plt.plot(months, sales, color='red',)
plt.show()

# months = np.array (["April","May", "June" , "July", "August", "September", "October" , "November" , "December", "January" , "February" , "March"])

# sales = np.array( [20078, 20287 , 19982 , 20271 , 20184 , 20265 , 20314 , 20373 , 20168, 20371 , 20207 , 19897 ,])

# plt.figure(figsize=(15,20))
# plt.bar(months,sales)
# plt.ylim(19500, max(sales))
# plt.ylabel("Sales")
# plt.xlabel("Months")
# plt.plot(months, sales, color='red', marker='o', linewidth=2, label='Trend Line')
# plt.show()

