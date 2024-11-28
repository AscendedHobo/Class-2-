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


counter = 0


if type.lower() == "f":

    while counter <= 10:
        counter += 1
        Fans = Fans + 1
        fconvert = float(Fans-32)*5/9
        print(fconvert)


elif type.lower() != "f":
    while counter <= 10:
        counter += 1
        Cans = Cans + 1
        Cconvert = float(Cans-32)*5/9
        print(Cconvert)




