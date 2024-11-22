import random

print(random.randrange(3, 9)) # integer 3 to 9 (excludes 9)
print(random.randint(3, 9)) # Integer 3 to 9 (includes 9)
print(random.random()) # a float between 0.0 and 1.0
print(random.uniform(20, 60)) # float between 20 and 60, inclusive


import random

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) # chose from a list
print(random.shuffle(mylist)) # randomly shuffle a list
print(mylist)
print(random.sample(mylist, k=2)) # pick a sample of 2 from list

