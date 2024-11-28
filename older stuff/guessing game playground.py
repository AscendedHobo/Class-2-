# program to test average of finding a number using binary chop

import random

gamesplayed = 0

resultlist = []


numberlist = []

#create a list from 0 to min 100 max 2000
for i in range(0, random.randrange(100,2000)):
    numberlist.append(i)

# create guessing game

winningnumber = random.choice(numberlist) # Picks a random number from the random list

## create guessing formula
guessingIndex = len(numberlist) // 2  ## gets the len of random list and halfs it to find middle NOTE IS INT FAILING COMPUTE ON ODD NUMBER LISTS

guessingNumber = numberlist[guessingIndex] ## uses that half number to get a vaule



while guessingNumber != winningnumber:
    guessingIndex = len(numberlist) // 2  # Compute the middle index
    guessingNumber = numberlist[guessingIndex]  # Get the middle value
    
    if guessingNumber > winningnumber:  # Guess too big
        numberlist = numberlist[:guessingIndex]  # Take the left half
    elif guessingNumber < winningnumber:  # Guess too small
        numberlist = numberlist[guessingIndex:]  # Take the right half



print("Correct!")

       
