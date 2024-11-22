# definitions
drinksList  = [ ["Coffee", 2.0, ], ["Tea", 1.5]   ,  ["Milk", 1.5 ] ]
extrasList  = [ [ "Sugar", .1 ], ["Honey", .5] ]
foodList    = [ [ "Toast", 2 ], ["Eggs", 2] ]
 
 
def printLists():
 
    myLists = [ drinksList, extrasList, foodList]
    print(len(myLists))
    for x in range(0 , len(myLists)):
        printList(myLists[x])
 
def printList(incomingList):
    for i in range(0, len(incomingList)):
        print(incomingList[i])
 
def buildList(inpDesc, incomingList):
 
    inpName = "xxx"
    while inpName != "" :
        inpName = input(f"Enter {inpDesc}'s name (blank to exit):")
        if inpName != "":
            inpPrice = input(f"Enter {inpName} price: ")
            incomingList.append(  [inpName, inpPrice] )
 
#--------------------------------
 
 
# print the table
printLists()
 
# build the drinks list
buildList("drink",  drinksList)
 
# adding extras
buildList("extra", extrasList)
 
# print the table
printLists()
 
# order the drink
 
 
 