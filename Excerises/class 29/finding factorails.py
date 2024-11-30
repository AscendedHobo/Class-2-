'''
Write a Python program to print the factorial of a number.
1. The factorial of a number, for example 5, is calculated as
5 * 4 * 3 * 2 * 1 = 120.
1. Ask the user to input an integer greater than zero.
2. Calculate and print the factorial of that integer.
3. Can you write this as a recursive function. i.e. a function that calls itself?
'''

#usernumber = int(input("Choose a number : "))
usernumber = 5
                 
for i in range (0, usernumber- 1 ):
    usernumber = usernumber * i
    print(usernumber)

print(usernumber)