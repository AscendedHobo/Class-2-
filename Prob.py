## lotto number picker
import random
lottorange = 12

lottlist = []
for i in range(1,lottorange):
    lottlist.append(i)


winninglist = []

for i in range(0,6):
    winchoice = random.choice(lottlist)
    winninglist.append(winchoice)
    lottlist.remove(winchoice)

print(winninglist)

userguesslist = []

for i in range(0,6):
    userchoice = int(input(f"Pick a number between 1-{lottorange}: "))
    if userchoice in userguesslist:
            userchoice = int(input("That number is already choosen try again : "))
    else:
         userguesslist.append(userchoice)


userguesslist = set (userguesslist)
winninglist = set (winninglist)

print(f" winning numbers are {winninglist}")
print(f" winning numbers are {userguesslist}")


overlap = userguesslist & winninglist

if len(overlap) > 0:
    matchingnumber = len(overlap)
    percentlist = []

    for i in range(0, matchingnumber):
        #  percentlist.append((1/lottorange).round())
        percentlist.append(round(1 / lottorange,10 ))  # Replace 'x' with the number of decimal places

        lottorange -= 1
        
    print(percentlist)

    total = 1
    for i in percentlist:
        total = i * total

    print(f" you got {len(overlap)} numbers correct, that was a {total*100}% chance to get that many")
else:

    changingrange = lottorange
    percentlist =[]


    for i in range(0 , lottorange):
        percentlist.append(round((changingrange - 6) / changingrange, 10))

    total = 1
    for i in percentlist:
            total = i * total

    print(f" you got {len(overlap)} numbers correct, that was a {total*100}% chance to get that many")

#  import fractions as fr
 
# num = 1/2 + 1/3 + 1/133

# print(num)

# frac = fr.Fraction(num).limit_denominator()

# print(frac)
 

# import random
 
# numberSpace = []   # numbers 1 to 50
# computer = [] # 6 numbers from the numberSpacelist
# player=[]
 
# # generate probabilty space.. numbers (1 to 50).. do we need do this?
# for x in range(1, 51):
#     numberSpace.append(x)
 
# # computer's pick of 6 numbers
# computer = random.sample(numberSpace,k=6)
# computer.sort()
# print(computer)
 
# # player's pick of 6 numbers
# player = random.sample(numberSpace,k=6)
# player.sort()
# print(player)
 
# # convert to sets further manuipualtion
# computer = set((computer))
# player= set((player))
# matched = set((computer & player))
# print(f"You got {len(matched)} matching number(s) = {computer & player}")
 














