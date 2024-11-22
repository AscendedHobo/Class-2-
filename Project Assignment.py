'''
you could simulate the number of people randomly arriving at a supermarket checkout
and calculate the average time taken to serve them

'''
import random

names = ["Alexander", "Olivia", "Benjamin", "Sophia", "Ethan", "Amelia", "Noah", "Isabella", "Liam", "Charlotte"]


while len(names) > 0:
    print(names)
    removename = names[random.randint(0,len(names))]
    print(f"Name to remove is {removename}")
    names.remove(removename)
    print(names)
