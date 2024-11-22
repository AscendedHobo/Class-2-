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
 
    
 
 