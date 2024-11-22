tea_price = 2
cof_price = 5
milk_price = 3
hotChoc_price = 2


Headings = [
    f"¦ We serve the following Drink options \t ¦",
    f"¦ Tea             ¦ £{tea_price}",
    f"¦ Milk            ¦ £{milk_price}",
    f"¦ Hot Choc        ¦ £{hotChoc_price}",
    f"¦ Coffe           ¦ £{cof_price}", ]


lenHeadings = len(Headings[0]) - 2
print(lenHeadings)

dashes = f"¦{lenHeadings * '-'}¦"

print(dashes)
for heading in Headings:

    index = Headings.index(heading)

    if index == 0:
        print(heading)
    else:
        lenHeadTea = len(Headings[index])
        differnce = lenHeadings - lenHeadTea + 1
        extraSpaces = f"{differnce * ' '}"
        print(f"{Headings[index]}{extraSpaces}¦")


print(dashes)

# Standard String
Variable_name = "Whatever characters in these quotation marks "
# to print an String
print("this here")
