# Program to process elements in an array

# list of numbers
myNumbers = [34, 23, 34, 54, 56, 67]
# index =    0  1  2  3  4   5

# print the list of numbers
print(myNumbers)
print("Number of Items  : ", len(myNumbers))


# NB : list contain duplicate values!

# print the elements, one by one
for element in myNumbers:
    position = myNumbers.index(element)  # get position of the element
    print(position, element)
