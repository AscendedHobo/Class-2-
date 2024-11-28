'''
    Program to calculate variance and std dev of a set
    of random integers.
 
    Date : 26/11/2024
'''
 
import random
import math
 
myNumbers = []
 
def genRandNumbers():
    ''' Generate a list of 99 random integers in the range 30 to 50.'''
 
    total=0
    myNumbers.clear()
    for x in range(1, 10000):
        number = random.randint(30, 50)
        total += number
        myNumbers.append(number)
 
    mean = total / len(myNumbers)
    myNumbers.sort()
    #print(myNumbers)
    print("Mean : ", mean)
    return mean
 
def calcStats():
    ''' Calculate and print the variance of the list '''
    mean = genRandNumbers()
 
    total = 0
    for x in range(0, len(myNumbers)):
        diff = myNumbers[x] - mean
        squared = diff ** 2
        total += squared
    meanSquared = total / len(myNumbers)
 
    print("variance : ", meanSquared)
    print("std Dev : ", math.sqrt(meanSquared))
 
 
#--- MAIN SECTION ----------------------------
 
# Run your program 5 times.
for x in range(0,5):
    calcStats()