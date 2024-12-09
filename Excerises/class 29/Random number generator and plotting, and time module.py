
# # Relative Frequency - rolling a dice
# import numpy as np
# from matplotlib import pyplot as plt
# # create a dataset of size=N, of integers 1 to 6
# a = np.random.randint(low=1, high=6, size =(200))
# # Create frequency histogram of each integer
# np.histogram(a, bins = [1,2,3,4,5,6])
# hist, bins = np.histogram(a, bins = [1,2,3,4,5,6])
# # printing histogram
# print(hist)
# print(bins)
# # plot the histogram
# fig1 = plt.figure(figsize =(5, 5))
# plt.hist(a, bins = [1,2,3,4,5,6])
# plt.title("Frequency Histogram")
# plt.show()

#########################################################

# # Relative Frequency - coin flip

# import numpy as np
# from matplotlib import pyplot as plt
# # create a dataset of size=N, of integers 1 to 6
# a = np.random.randint(low=1, high=2, size =(4))
# # Create frequency histogram of each integer
# np.histogram(a, bins = [1,2])
# hist, bins = np.histogram(a, bins = [1,2])
# # printing histogram
# print(hist)
# print(bins)
# # plot the histogram
# fig1 = plt.figure(figsize =(5, 5))
# plt.hist(a, bins = [1,2])
# plt.title("Frequency Histogram")
# plt.show()
#########################################################

# import numpy as np
# from matplotlib import pyplot as plt
# # create a dataset of size=N, of integers 1 to 6
# a = np.random.randint(low=1, high=6, size =(200))
# # Create frequency histogram of each integer
# np.histogram(a, bins = [1,2,3,4,5,6])
# hist, bins = np.histogram(a, bins = [1,2,3,4,5,6])
# # printing histogram
# print(hist)
# print(bins)
# # plot the histogram
# fig1 = plt.figure(figsize =(5, 5))
# plt.hist(a, bins = [1,2,3,4,5,6])
# plt.title("Frequency Histogram")
# plt.show()


#########################################################
### 2024-12-09 Roll a die
import numpy as np, matplotlib.pyplot as plt

 
# dice_rolls = np.random.randint(1,7,1000)
# dice_vals, dice_counts = np.unique_counts(dice_rolls)
# print(dice_vals,dice_counts)
# plt.bar(dice_vals,dice_counts)
# plt.show()

#########################################################
# dice_rolls = np.random.randint(1,3,1000)
# dice_vals, dice_counts = np.unique_counts(dice_rolls)
# print(dice_vals,dice_counts)
# plt.bar(dice_vals,dice_counts)
# plt.show()
#########################################################

# card variantion

# dice_rolls = np.random.randint(1,53,100)
# dice_vals, dice_counts = np.unique_counts(dice_rolls)
# print(dice_vals,dice_counts)
# plt.bar(dice_vals,dice_counts)
# plt.show()


## working out chance of pulling any given unquie card one after another

import random

cardlist = []

for i in range ( 0,53):
    cardlist.append(i)

    # list is created, we now want to print the chance of pulling a unique  number


cardlistlen = len(cardlist)

for i in range(0,cardlistlen):
    choicetopop = random.choice(cardlist)
    cardlist.remove(choicetopop)
    print(f"Removed {choicetopop}")
    print(f"the chance of pulling any given card is now {1/len(cardlist)*100}% ")
    


# cardpull = np.random.randint(1,53,100)
# dice_vals, dice_counts = np.unique_counts(dice_rolls)
# print(dice_vals,dice_counts)
