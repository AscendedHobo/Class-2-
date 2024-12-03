'''Write a Python program to check the random number generater.
1. If a random number generator is truly random each number generated should occur
the same number of times.
2. Create a list of 500 numbers in the range 1 to 20.
3. Count the frequency of each number, i.e. the number of times the integer occurs in
the list.
4. Calculate the mean of the frequencies.
5. Plot the random numbers and their frequencies in a suitable chart.
'''


import  random
import numpy as np
import matplotlib as mp



numlist = []

for i in range(0,20):
    numlist.append(random.randint(1, 20))

print(numlist)

freqencylist = []

for i in numlist:
    freqencylist.append(i)
    freqencylist.append(numlist.count(i))

print(freqencylist)


total = 0
for i in (freqencylist[::2]):
    total = total + i

mean = total / (len(freqencylist) / 2)


print(mean)



#empty list

# append checking number to that list
# appended count of checking number to that list

# list needs to be sorted into mini lists of two
# or create sublists in the first place per i vaule / loop?


# a