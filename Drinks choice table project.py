


# user will make a drinks menu 

# ask inputs for drinks to make a list,additives to use,  along with the price to charge for those items

# the choices will be put into a table that auto frames the size of the items put into it

##  it will then begin a choice selection, phase, user inputs the choices and a total cost will be displayed at every step

##  the user will be able to reset back to the starting choice of the drink at any point
##  a question will be asked for the temperture of the drink, and a conversion to C or F
### the user will then be prompted to give that combo a name, which will be saved into a list 
### prompt to confirm or cancel the order once the drinks and additives are chosen,

##  neat animations using time delay will print charater images after each selection
##    

#####################################

# welcoming and introduction to the menu building process
#############print(f"Hello {U_name} Lets build an amazing drinks menu together! ")
drink_number = int(input(f"To begin lets build a list of your favourite drinks, how many would you like to add to the menu? :"))


###making variables for the for loop
drinkcounter = 0
Drinklist = []

for drink in range(0, drink_number):  #   uses answer of drink number input to decide range of times to loop
    drinkcounter += 1  #  counts the drink number input of the user increases per one each loop
    drink = (input(f"Enter drink name {drinkcounter} : ")).lower()  #  increases  input of user and reminder of what number they are on
    Drinklist.append(drink)  ## creates a list of the drink names

print("Quality drink choices, Lets set a price for each one") 

##  like the above, for range of the items entered in drinks list, loop input for prices of each item drinkslist and make that separate list
Drinks_price_list = []
for price in Drinklist:
    drinksprice = float(input(f"How much is {price} : £"))
    Drinks_price_list.append(drinksprice)

print(f"Boring plain drinks wont do! lets make a list of extras to go with! ")

extralist = []
extraprice = []
addingextra = ""
while addingextra != "exit":
    extra = (input("Add a extra (Exit to finish) : ")).lower()
    if extra == "exit":
        break
    extralist.append(extra)

for price in extralist:
    extra_price = float(input(f"How much is {price} : £"))
    extraprice.append(extra_price)
    

 ## we now have 4 lists, drinks, drinks price, extras , extra prices.
 ##  time to recap to the user everything so far in a nice table


maxlength = [len(Drinklist), len(extralist)]
maxlength.sort()
maxlength = (maxlength[-1]+1)


heading = f"|Drink name |\t Drink price |\t Extra name |\t extra price |"
print("-" * (len(heading) + 5))  

print(heading)
print("-" * (len(heading) + 5))

for i in range(maxlength):
    try:                                        ######## try block incase drinks and extra lists be different lengths 
        drink = Drinklist[i]
        drinkprice = Drinks_price_list[i]
        extra = extralist[i]
        extra_price = extraprice[i]
        print(f"|{drink:<15}|  \t £{drinkprice:<11}| \t {extra:<15}|  \t £{extra_price:<11}| ")
    except IndexError:
        continue
print("-" * (len(heading) + 5))


print(f"Lets place an order!")

cost = 0.00
Validchoice = False

while Validchoice == False:

    drinkchoice = (input("Choose a drink : ")).lower()
    if drinkchoice in Drinklist:
        priceindex = Drinklist.index(drinkchoice)
        cost += Drinks_price_list[priceindex] 
        Validchoice = True
        print(f"Current total is {cost}")
    else:
        print("Error: please pick an Drink from the table")


wantextra = (input("Would you like an extra with that? (yes no)")).lower()

chosen_extra_list = []

while wantextra == "yes":
    choiceextra = (input("Which extra would you like? : ")).lower()
    if choiceextra in extralist:
        priceindex = extralist.index(choiceextra)
        cost = cost + extraprice[priceindex]
        extrachoice = choiceextra
        chosen_extra_list.append(choiceextra)
        print(f"Current total is {cost}")
        wantextra = (input("Would you like to add another extra? yes no? : ")).lower()

    else:
        print("Error: please pick an Extra from the table")





print(f"You have chosen {drinkchoice} with extra {chosen_extra_list} : the total cost is £{cost} ")



    





