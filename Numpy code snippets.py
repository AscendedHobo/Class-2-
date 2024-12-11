import numpy as np

###########################################################################################

# # populate array with integers in a range, in steps of 3
# import numpy as np

# minVal = 30
# maxVal = 60
# stepVal = 3
# myArray = np.arange(minVal, maxVal, step=stepVal)
# print(myArray)

###########################################################################################

#### Random number generating in numpy

# generate 20 random numbers from Normal distribution,
# # with mean 0 and stdDev = 1 (includes negative numbers)
# randNum = np.random.normal(0,1,15)
# print(randNum)
# # generate 12 random integers in range 20 to 30
# randNum = np.random.randint(20, 30,12)
# print(randNum)
# # generate 10 rand numbers and choose 4, duplicates allowed
# print(f"Random Choice -Dups : {np.random.choice(10, 8)}")
# # generate 10 rand numbers and choose 4, duplicates NOT allowed
# print(f"Random Choice -noDups: {np.random.choice(10, 8, replace=False)}")


############################################################################################

# filtering arrays - conditions

# # filter an array
# myArray = np.array([[5.54, 3.38, 7.99],
# [3.54, 4.38, 6.99],
# [1.54, 2.39, 9.29]])
# print(f"Filter this : \n{myArray}")
# print(f"All values > 5 {myArray[myArray > 5]}")

############################################################################################

# Slicing arrays

# import numpy as np

# Create an array
# arr = np.array([10, 20, 30, 40, 50, 60])

# # Slicing the array
# slice_1 = arr[1:4]   # Extract elements at indices 1, 2, 3 (start:stop, stop is excluded)
# slice_2 = arr[:3]    # Extract elements from the start to index 2 (0, 1, 2)
# slice_3 = arr[3:]    # Extract elements from index 3 to the end
# slice_4 = arr[::2]   # Extract every second element (step = 2)

# # Modify the slice
# arr[1:4] = [99, 88, 77]  # Modify indices 1, 2, 3 directly

# # Outputs
# print("Original array after modification:", arr)  # [10, 99, 88, 77, 50, 60]
# print("Slice 1 (arr[1:4]):", slice_1)            # [99, 88, 77]
# print("Slice 2 (arr[:3]):", slice_2)             # [10, 99, 88]
# print("Slice 3 (arr[3:]):", slice_3)             # [77, 50, 60]
# print("Slice 4 (arr[::2]):", slice_4)            # [10, 88, 50]

############################################################################################

# Shaping

# # generate 12 random integers in range 20 to 30
# randNum = np.random.randint(20, 30,12)
# print(type(randNum))
# print(randNum)
# print(randNum[1])
# # rearange those 12 numbers as a 3 by 4 matrix
# print(randNum.reshape((6,2)) )
# # print(f"shape = {randNum.reshape((6,2)).shape}" )
# print("-" * 60)
# # print(f"shape = {randNum.reshape((2,6)).shape}" )
# print(randNum.reshape((2,6)) )


############################################################################################


# x = np.array([1,5,3,6,7])
# y = np.array([2,3,2,5,3])
# # multiply 2 arrays of integers, element by element
# print(f"{x} * {y} = {x * y}")
# # multiply all elements by same number
# print(f"{x} * {3} = {x * 3}")
# # add 2 arrays of integers, element by element
# print(f"{x} + {y} = {x + y}")

############################################################################################


# Date functions in NumPy

# print(f"The year it all started: {np.datetime64(0, 'Y')}")
# print(f"Twelve days of Xmas : {np.arange('2024-12-14', '2024-12-26', dtype='datetime64[D]')}")
# print(f"Days to Xmas : { np.datetime64('2024-12-25') - np.datetime64('today', 'D') }")



# # Define today's date
# today = np.datetime64('today', 'D')
# print("Today: ", today)

# # Define tomorrow's date
# tomorrow = today + np.timedelta64(1, 'D')
# print("Tomorrow: ", tomorrow)


############################################################################################


