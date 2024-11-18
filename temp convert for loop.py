# farenheit to celuis converter
#

##ask  if wish to C to F or F to C

type =  str(input("start with C or F ? :"))


if type.lower() == "f":
    Fans = float(input("insert the number :"))

else:
    Cans =int(input("insert the number :"))

if type.lower() == "f":
    fconvert = float(Fans-32)*5/9
    print(f"the converted is {fconvert}")

else:
    Cconvert = float(Cans*9/5)+32
    print(f"the converted is {Cconvert}")


print("The next ten conversions will be")




if type.lower() == "f":

    for x in range(0,10):

        Fans = Fans + 1
        fconvert = float(Fans-32)*5/9
        print(fconvert)


elif type.lower() != "f":
    for x in range(0,10):
        Cans = Cans + 1
        Cconvert = float(Cans-32)*5/9
        print(Cconvert)




