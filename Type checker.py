""" 
Program to Validate and Accept a Floating Number
Author : Komal, Sayful, Alan
Written: 15/Nov/2024
 
Program using arrow functions
 
"""


def get_integer_input() -> float:
    ''' 
        purpose : to accept a floating number 
    '''
    user_input = input("Enter a number: ")
    try:
        value = float(user_input)
        return value
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


# ---------------------------------

myNumber = ""
while type(myNumber) != float:
    myNumber = get_integer_input()

print(myNumber)
