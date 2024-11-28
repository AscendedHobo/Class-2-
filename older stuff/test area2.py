import random
import math

loops = 0

while loops <5:

    num = []

    for i in range(0,10):
        num.append(random.randint(30,40))


    total = 0
    for i  in range(len(num)):
        total = num[i] + total


    mean = total / len(num)
    print(f"The mean is {mean}")

    num.sort()

    variance = []

    for i in range(len(num)):

        Var = num[i] - mean

        Var = Var * Var

        variance.append(Var)


    total = 0
    for i  in range(len(variance)):
     total = variance[i] + total

    meanofvar = total / len(variance)

    print(f" The variance is  {meanofvar}")

    print(f" The Standard dev = {math.sqrt(meanofvar)}")
    
    loops += 1



print(num)
countlist = []
dupelist = []
for i in num:
    counter = num.count(i)
    if counter > 1:
        dupelist.append(i)
        dupelist.append(counter)


print(dupelist)
# Break list in sets of 2

# Break list into sets of 2
pair_list = [dupelist[i:i+2] for i in range(0, len(dupelist), 2)]
print(pair_list)


pair_list = []

for i in range(len(dupelist)):
    pair_list = (dupelist[i:i+2])

print(pair_list)


print(f"")


numberlist = [0,6,9,8,7,4,5,6,9,7]

random.shuffle(numberlist)

sorted = False

while sorted ==  False:
    for i in range (len(numberlist)):
        if i < i+1:
            print(f"List is sorted {numberlist}")
            sorted = True

