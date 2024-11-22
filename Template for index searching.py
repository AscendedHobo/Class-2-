# Program to search a list
 
namesList = ["Mark", "Abbey", "Fred", "Wilma", "Abbey" ]
 
 
# search the list
searchName = input("Enter name to search for: ")
 
if searchName in namesList:
    location = namesList.index(searchName)
    print(f"{searchName} found at position:" , location)
else:
    print(f"{searchName} not found")
 

 #quick check for if answers is yes no y nonlocal
    
#yesno = ["yes", "Yes" , "no", "No", "y", "Y", "n" , "N"]