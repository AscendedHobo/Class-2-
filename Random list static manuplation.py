

import random

namelist = []


namelist.append(random.randint(0,20))

print(namelist)

print("-" * 30)
##making the list
for x in range(0,9):
    x = namelist.append(random.randint(0,20))

print(namelist)

print("-" * 30)
### calculating mean

total = 0

for i in range(0,len(namelist)):
    total = total + namelist[i]

print(total)
   
mean = total / len(namelist)

print(f"the mean is {mean}")


print("-" * 30)


## calcuating the median

namelist.sort()
print("List has been sorted")
print(namelist)

## if list len is even then
if len(namelist) % 2 == 0:

    indexfinder1 = int((len(namelist)) / 2) -1
    indexnumber1 = namelist[indexfinder1]

    indexfinder2 = int((len(namelist)) / 2)
    indexnumber2 = namelist[indexfinder2]

    medain = (indexnumber1 + indexnumber2) / 2
    
    print(medain)
else:      #### if not even then odd
    indexfinder = int(len(namelist)) / 2

    medain = namelist[indexfinder]

    print(mean)
