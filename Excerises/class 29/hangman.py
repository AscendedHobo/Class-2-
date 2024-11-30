'''
Write a Python program to play the popular game of Hangman.
1. Set up a list of words of various lengths, which may be related to a particular topic.
2. Randomly select one word from this list and display a number of “_”s representing each
letter of the chosen word.
3. The user will then have 10 attempts to enter letters of the alphabet and try to guess the
hidden word.
4. The user may enter the whole word if they think they have guessed it.
5. If the user’s letter is contained in the hidden word then replace all corresponding “_” with
that letter.
6. If the user’s letter is not contained in the word, then add it to a list of letters the user has
tried already.
7. Continue the game until the user has guessed the word or has had 10 attempts.

'''
import random

words = ['correlation', 'covariance', 'variance', 'causality', 'scatter', 'plot', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'data', 'analysis', 'statistics', 'regression', 'machine', 'learning', 'visualization', 'heatmap', 'cleaning', 'processing']

randomword = random.choice(words) 

print("_" * 60)

# underscorelist = []
# for i in range(len(randomword)):
#         underscorelist = underscorelist.append("_")

underscorelist = list("_" * len(randomword))


charalist = []

for i in range (0,len(randomword)):
    charalist.append(randomword[i])

print(charalist)

trycount = 0 

listcomplete = False

trylist = []

print(underscorelist)

while trycount < 15 and listcomplete == False: 
    print(f"{underscorelist}")
    userinput = input("Enter a letter or attempt a whole word guess :" )
    trycount += 1

                     
    if userinput == randomword:
        print("You got the word")
        listcomplete = True
        print(f"You got the word in {trycount} guesses!")


    if userinput in charalist:
        for i in range(len(randomword)):
            # check index with input 
            if charalist[i] == userinput:
                underscorelist[i] = userinput


    if userinput in charalist:
        print(f"{userinput} is a correct guess!")
    else:
        print(f"{userinput} is a incorrect guess!")
        trylist.append(userinput)
    print(f"Not in  {trylist}")
    print(f"You have guessed {trycount} times limit reached ")

    if underscorelist == charalist:
        print("You got the word!!")
        print(f"You got the word in {trycount} guesses!")
        listcomplete =  True
