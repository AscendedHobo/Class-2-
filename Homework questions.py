

# #####################
# Exercise 1
# #####################
# Write a Python program that prints the integers between 1000 and 3000
# that are divisible by both 7 and 13.
 

 # llist betweeem 1000-3000
startlist = range(1000,3001)
 
 # making gllobal variables

createthirteenlist = []
createsevenlist = []


# make two lists in for x  divided 7 and 13

for x in startlist:
    createsevenlist.append(x / 7)
    createthirteenlist.append(x / 13)



fullsevenlist = []

for y in createsevenlist:
  
    if y is int:
        fullsevenlist.append(createsevenlist)

print(f"numbers divisable by 7 are : {fullsevenlist}")


fullthriteenlist = []

for x in createthirteenlist:
    
    if x.is_integer() :
        fullthriteenlist.append(createthirteenlist)

print(f"numbers divisable by 13 are : {fullthriteenlist}")





           
#for x in startlist:
#    createthirteen = x % 13

 
 
# #####################
# Exercise 2
# #####################
# Write a Python program that converts temperatures to and from Celsius and Fahrenheit.
# Formulas:
# c = (5/9) * (f - 32)
# f = (9/5) * c + 32
# c = temperature in Celsius, f = temperature in Fahrenheit
# Example:
# Enter degrees in F or C: 70F
# 70F is equivalent to 21.1C
# Enter degrees in F or C: 12C
# 12C is equivalent to 53.6F
 
 
 
# #####################
# Exercise 3                  NB : This will become offical assignment -- 2 weeks later
# #####################
# Write a Python program that guesses a number between 1 and 15,
# where the user is asked to guess the number.
# As long as the user guesses the wrong number, a new attempt should be made.
# When the correct number is guessed, the program should print
# "Correct guess after X attempts!" where X is the number of attempts made.
# Example:
# Guess a number (1-15): 4
# Wrong number
# Guess a number: 7
# Correct guess after 2 attempts.
 
 
# #####################
# Exercise 4
# #####################
# Write a Python program that uses nested for-loops to generate the following pattern:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
 

 for i in range(1,10):
    print(f"{i}"*i)
 
# #####################
# Exercise 5
# #####################
# Write a Python program that uses nested for-loops to print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
 
# #####################
# Exercise 6
# #####################
# Write a Python program that prints the letter 'A' as shown below:
#   ***
#  *   *
#  *   *
#  *****
#  *   *
#  *   *
#  *   *

