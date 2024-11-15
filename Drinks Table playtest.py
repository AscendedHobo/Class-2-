# list of Drinks and extra variables
Drinklist = ["Tea", "Coffee"]
Extra1 = "Milk"
Extra2 = "Sugar"

dashes = f"¦{60 * '-'}¦"


# prices
tea_price = 2
coffee_price = 3
milk_price = 0.50
sugar_price = 0.20

Price = 0

# added later when i realised i wanted it to loop for a reset order
while True:

    # Printing table
    print("¦" + (60 * "-") + "¦")
    print("We serve the following Drink options")
    print("¦" + (60 * "-") + "¦")
    print(f"¦Tea \t ¦£{tea_price}")
    print(f"¦Coffee \t ¦£{coffee_price}")
    print("¦" + (60 * "-") + "¦")
    print("¦We serve the following Extra options")
    print("¦" + (60 * "-") + "¦")
    print(f"¦Milk \t ¦£{milk_price}0")
    print(f"¦Sugar \t ¦£{sugar_price}0  ")
    print("¦" + (60 * "-") + "¦")

    # prompt what type of drink they want , from the list

    Drink_choice = str(input("Choose drink, Tea or Coffee :")).lower()

 # checks if the input is in the exsiting approved drinks list
    while Drink_choice not in Drinklist:
        print("Invalid option, please type Tea or Coffee")
        Drink_choice = str(input("Choose drink, Tea or Coffee :"))

    # i want to add a the price of the choosen item to price
   # if its equal to exactly Coffee adds coffee price otherwise adds the Tea price
    if Drink_choice == "Coffee":
        Price = Price + coffee_price

    if Drink_choice == "Tea":
        Price = Price + tea_price
 # moves onto a yes no for milk choice
    Extra1_choice = str(input("Would you like milk Yes or No? :"))
# if answer is in the list / accepted it will move onto pricing part otherwise loops for correct input
    while Extra1_choice not in ["Yes", "no", "yes", "no"]:
        print("Invalid answer, please type Yes or No : ")
        Extra1_choice = str(input("Would you like milk Yes or No? :"))

# simalar but different pricing coding if yes then adds price, otherwise price stays equal to old price
    if Extra1_choice == "Yes" or Extra1_choice == "yes":
        Price = Price + milk_price
    elif Extra1_choice == "No":
        Price = Price
# moves onto adding sugar or choice same as milk method above
    Extra2_choice = str(input("Would you like Sugar added? Yes or No :"))

    while Extra2_choice not in ["Yes", "no", "yes", "no"]:
        print("Invalid answer, please type Yes or No : ")
        Extra2_choice = str(input("Would you like Sugar added? Yes or No :"))

    if Extra2_choice == "Yes" or Extra2_choice == "yes":
        Price = Price + sugar_price
    elif Extra2_choice == "No":
        Price = Price

# recaps the order via an f string , tabled for neatness
    print("You have selected the following")
    print(f"   Drink:{Drink_choice} \t Milk:{
        Extra1_choice}  \t Sugar:{Extra2_choice}")

# shows the total updated price at this point
    print(f"Total price is £{Price}")
# option to restart the order if user want to change
    Restart_option = str(input("Confirm or Restart your order? :"))
# checks for valid input loops until true
    while Restart_option not in ["Restart", "restart", "Confirm", "confirm"]:
        print("Invalid option, please Type Restart or Confirm")
        Restart_option = str(input("Confirm or Restart your order? :"))

# if valid and confirm, thanks for order and exits program
    if Restart_option in ["Confirm", "confirm"]:
        print("Thanks for your order!")
        exit()
#  else sets the price back to 0 for re ordering and the first while loop closes/ restarts
    else:
        Restart_option == ["Restart", "restart",]
        print("Order cleared")
        Price = 0
