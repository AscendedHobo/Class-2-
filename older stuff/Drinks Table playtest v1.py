# list of Drinks and extra variables
Drinklist = ["Tea", "Coffee"]
Extra1 = "Milk"
Extra2 = "Sugar"


# prices
tea_price = 2
coffee_price = 3
milk_price = 0.50
sugar_price = 0.20

Price = 0
while True:

    # Printing table
    print(60 * "-")
    print("We serve the following Drink options")
    print(60 * "-")
    print(f"Tea \t £{tea_price}")
    print(f"Coffee \t £{coffee_price}")
    print(60 * "-")
    print("We serve the following Extra options")
    print(60 * "-")
    print(f"Milk \t £{milk_price}0")
    print(f"Sugar \t £{sugar_price}0  ")
    print(60 * "-")

    # prompt what type of drink they want , from the list

    Drink_choice = str(input("Choose drink, Tea or Coffee :"))

    while Drink_choice.lower() != "tea" and  Drink_choice.lower() != "coffee":
        print("Invalid option, please type Tea or Coffee")
        Drink_choice = str(input("Choose drink, Tea or Coffee :"))


    # i want to add a the price of the choosen item to price

    if Drink_choice == "Coffee".lower():
        Price = Price + coffee_price

    if Drink_choice == "Tea".lower():
        Price = Price + tea_price

    Extra1_choice = str(input("Would you like milk Yes or No? :"))

    while Extra1_choice not in ["Yes", "no", "yes", "no"]:
        print("Invalid answer, please type Yes or No : ")
        Extra1_choice = str(input("Would you like milk Yes or No? :")).lower()

    if Extra1_choice == "Yes" or Extra1_choice == "yes":
        Price = Price + milk_price
    elif Extra1_choice == "No":
        Price = Price

    Extra2_choice = str(input("Would you like Sugar added? Yes or No :"))

    while Extra2_choice.lower() != "yes" and Extra2_choice.lower() != "no" :
        print("Invalid answer, please type Yes or No : ")
        Extra2_choice = str(input("Would you like Sugar added? Yes or No :")).lower()

    if Extra2_choice.lower() == "Yes" or Extra2_choice == "yes":
        Price = Price + sugar_price
    elif Extra2_choice.lower() == "No":
        Price = Price

    print("You have selected the following")
    print(f"   Drink:{Drink_choice} \t Milk:{
        Extra1_choice}  \t Sugar:{Extra2_choice}")

    print(f"Total price is £{Price}")

    Restart_option = str(input("Confirm or Restart your order? :"))

    while Restart_option not in ["Restart", "restart", "Confirm", "confirm"]:
        print("Invalid option, please Type Restart or Confirm")
        Restart_option = str(input("Confirm or Restart your order? :"))

    if Restart_option.lower() == "confirm":
        print("Thanks for your order!")
        exit()
    else:
        Restart_option.lower() == "restart" 
        print("Order cleared")
        Price = 0
