mainlist = ["tea", 2 , "coffee" , 5 , "orange" , 6 , "milk" , 8 , "water" , 10]


Drinklist = []
pricelist = []

for x in mainlist:
    if type(x) == str:
        Drinklist.append(x)
    else:
        pricelist.append(x)



indexnumber = 0

for x in Drinklist:
    print(f"The Drink {Drinklist[indexnumber]} costs {pricelist[indexnumber]}")
    indexnumber += 1

