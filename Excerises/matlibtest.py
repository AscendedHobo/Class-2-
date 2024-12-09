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
import pandas as pd
import matplotlib.pyplot as mp

############################################################################################
##create random number list
numlist = []

for i in range(0,1000):
    numlist.append(random.randint(1, 20))

numlist.sort
############################################################################################

#convert random list into list with the counted frequency next to it

freqencylist = []
for i in numlist:
    freqencylist.append(i)
    freqencylist.append(numlist.count(i))

############################################################################################
# working out the mean
total = 0
for i in (freqencylist[::2]):
    total = total + i

mean = total / (len(freqencylist) / 2)

print(mean)
############################################################################################
#Separating the one list into two lists
numlist = []
freqlist =[]
for i in range(0,(len(freqencylist)-1), 2):
    if i not in freqencylist:
        numlist.append(freqencylist[i])
        freqlist.append(freqencylist[i+1])
    
############################################################################################
# ploting the graph

mp.bar(numlist, freqlist)
mp.xlabel("Number")
mp.ylabel("Frequency")
mp.show()

############################################################################################
