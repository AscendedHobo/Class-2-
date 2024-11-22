import random

playagain = "yes"   # variable for the start again loop question


while playagain == "yes":       
    ##create list
    numberlist = []
    for i in range(0,101):
        numberlist.append(i)
# program chooses a random vaule from the list
    randomnumber = random.choice(numberlist)
#############################################################


# creates usernumber to be used as a condition for the while loop - note it has to be out of the range
    usernumber = 101

# creates vaule of counter
    counter = -1

    # starting a while loop checking usernumber vs random number
    while usernumber != randomnumber:
        counter = counter + 1
        print(f"You have tried {counter} times so far")
        usernumber = int(input("Enter a number between 0-100: "))

        if usernumber > randomnumber:
            print("number to high try again")
        elif usernumber < randomnumber:
            print("Number to low try again")
        else:
            print(f"Correct number was guessed after {counter} attempts")
            playagain = input("Would you like to try again ? (yes no) :")
            



print("Thanks for playing")



###to play itself
generate a list between 0 and random range up to 2000


use a for loop to make a list of those numbers
    
make the random choice

make the user input be from a the len of the list / 2

if that score is to high, make a new list in the range of the list 0 to listlen /2

