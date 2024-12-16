import numpy as np

# ############################################################################################

# # Create a 3 by 4 NumPy matrix of random integers
# # ▪ Use NumPy to find the min, max and mean of the entire 3 X 4 matrix
# # ▪ Show your results by printing the matrix and its min, max and mean.
# # ▪ Write the minimum amount of code.



# ## creating the array
# randomlist = np.random.randint(1,100,12)
# print(randomlist.reshape(3,4))
# print(f"The min is {randomlist.min()} the max is {randomlist.max()} the mean is {randomlist.mean()}")

# ############################################################################################

# Python has its own date and time methods. However, NumPy does too.
# Use the code to print yesterday’s date.
# Use this code to print the date one week from today.
# Use the code to generate all the dates from today to next week. 

# print(f"Yesterdays Date  : { np.datetime64('today', 'D') - 1 }")

# print(f"One week from now   : { np.datetime64('today', 'D') +7  }")

# # using for loop
# for i in range (0,7):
#     print(np.datetime64('today', 'D') + i)

# ##using arange 

# print(f"{np.arange(np.datetime64('today', 'D'), (np.datetime64('today', 'D')+7), dtype='datetime64[D]')}")



# ############################################################################################

# Write a program that uses NumPy to
# - generate an array of random numbers from 1 to 100, shaped as a 4 x 4 matrix
# # - Calculate the root of each number
# - Print your results

# randomnumber = np.random.randint(1,100,16).reshape(4,4)

# squared = np.sqrt(randomnumber)
# print(randomnumber)
# print(squared)

# ############################################################################################

# Write a NumPy program that
# - Generates a 4 X 4 array of random integers
# - Uses the code below to find the sum of each row
# - Prints the sum of each row.

# randomnumber = np.random.randint(1,100,16).reshape(4,4)
# print(randomnumber)

# row_sum = np.sum(randomnumber, axis =1)

# print(row_sum)


############################################################################################

# Write a NumPy program that
# - Generates a 4 X 4 array of random integers
# - Uses the code below to find the mean of each row
# - Prints the mean of each row.
# - How would you subtract the row-mean from each value o the row it represents?



randomnumber = np.random.randint(1,100,16).reshape(4,4)

row_means = np.mean(randomnumber, axis=1 ,  keepdims=True)
print(randomnumber)
print(row_means)


print("-" * 60)


arrayminusmean = []

for i in range (0,4):
    randomnumber[i]
    print(row_means[i])
    for j in range(0,4):
        randomnumber[i][j] = randomnumber[i][j] - row_means[i]
        arrayminusmean=np.append(arrayminusmean ,randomnumber[i][j])


print(arrayminusmean.reshape(4,4))

print("-" * 60)
print("|" * 60)
randomnumber = np.random.randint(1,100,16).reshape(4,4)
row_means = np.mean(randomnumber, axis=1 ,  keepdims=False)
arrayminusmean = []
for i in range (0,4):
    randomnumber[i]
    print(row_means[i])
    for j in range(0,4):
        randomnumber[i][j] = randomnumber[i][j] - row_means[i]
        arrayminusmean=np.append(arrayminusmean ,randomnumber[i][j])


print(arrayminusmean.reshape(4,4))
############################################################################################

