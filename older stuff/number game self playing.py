## program to test average of finding a number using binary chop

import random

resultlist = []

playagain = "y"

while playagain == "y":
    gamesplayed = 0
    while gamesplayed != 50:
        numberlist = []

        #create a list from 0 to min 100 max 2000
        for i in range(0, random.randrange(100,2000)):
            numberlist.append(i)

        # create guessing game

        winningnumber = random.choice(numberlist) # Picks a random number from the random list

        ## create guessing formula
        guessingIndex = len(numberlist) // 2  ## gets the len of random list and halfs it to find middle 

        guessingNumber = numberlist[guessingIndex] ## uses that half number to get a vauley
        trycount = 0
        ## game loop
        while guessingNumber != winningnumber:
            guessingIndex = len(numberlist) // 2  # Compute the middle index
            guessingNumber = numberlist[guessingIndex]  # Get the middle value
            trycount += 1

            if guessingNumber > winningnumber:  # Guess too big
                numberlist = numberlist[:guessingIndex]  # Take the left half
            elif guessingNumber < winningnumber:  # Guess too small
                numberlist = numberlist[guessingIndex:]  # Take the right half

            else:
                resultlist.append(trycount)
                print(F"Correct number selected after : {trycount}")
                trycount = 0
                gamesplayed += 1

    # after 50 games played we will do calulcation on the games played table and then prompt to run more games


    for i in resultlist:  ### maybe len?
        mean = resultlist[i] 

    print(f"{len(resultlist)} Games have been played the current average number of guesses to get the correct number is {mean} ")

    
    playagain = input(f"Play more games? (Y / N) : ").lower()


print("Thanks for checking")