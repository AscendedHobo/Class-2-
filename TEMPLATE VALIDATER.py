<<<<<<< HEAD:TEMPLATES/TEMPLATE VALIDATER.py
validDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "."]

thestring = input("Enter numbers: ")

validinput = True

for character in thestring:
    if character in validDigits:
        validinput = True

    else:
        validinput = False
        print("Invalid Character Detected")
        break

print(f"Input was {validinput}")


mynumber = int(input())

if mynumber is int:
    print("valid input")
else:
    print("invalid input")
=======
#------------------------------------------------------

# Vending Machine

#----------------------------------------------------
 
drinksMenu = [ "Coffee", 3.5, "Tea   ", 2.0, "Hot Choc", 3.0, "Hot Milk", 4.0 ]
 
# print the drinks' menu

def printMenu():
 
    print(20 * "-")
 
    for index in range(0, len(drinksMenu), 2):      # range(start, stop , step)
 
        drinkName = drinksMenu[index]

        drinkPrice= drinksMenu[index + 1]

        print(f" {int(index/2 + 1)} {drinkName} \t\t {drinkPrice}" )

    print(20 * "-")
 
 
 
# get the user to enter their drink selection

def enterChoice():
 
    userChoice = int(input("please make your selection: "))

    # validate user's choice, etc

 
 
#----------------------------------------

#       Main Processing Control starts Here

#-----------------------------------------
 
# print the drinks' menu

printMenu()
 
# get user's selection

enterChoice()
 
    
 
 
>>>>>>> ff02bf254c26f55e44c7b6be261bcdfdc561be0e:test area2.py
