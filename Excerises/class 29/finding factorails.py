'''
Write a Python program to print the factorial of a number.
1. The factorial of a number, for example 5, is calculated as
5 * 4 * 3 * 2 * 1 = 120.
1. Ask the user to input an integer greater than zero.
2. Calculate and print the factorial of that integer.
3. Can you write this as a recursive function. i.e. a function that calls itself?
'''



def factorial(number):
    total = number
# get starting number
    while number >= 1:
        total = total * (number-1)
        number -= 1
        if number == 1:
            print(f"The factorial of that is {total}")

number = int(input("type a whole number : "))
print(f"For the number {number}")
factorial(number)


def factorial(number):
    if number == 1:  # Base case: when the number is 1, the factorial is 1
        return 1
    else:  # returns number * the next 
        return number * factorial(number - 1)

# Get user input
number = 5

result = factorial(number)
print(f"The factorial of {number} is {result}")

## question for teacher, explaining the later steps of the factorial functon stepping through 



    