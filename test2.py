### Data structure types

names = []

username = ""

while username != "exit":
    username = input("Type a name to add to list : (type exit to end) :")
    if username != "" and username != "exit":
        names.append(username)
   
### sort list
names.sort()
## print names to be seen sorted
for name in names:
    print(name)


###  searching method 1 if statements with in list logic

user_search = ""
while user_search != "exit":
    user_search = input("m1 Search for a name in the list (exit to end) :")
    if user_search != "" and user_search != "exit":
        if user_search in names:
            print(f"Yes {user_search} is saved in the list in postion {names.index(user_search)} ")
        else:
            print(f"no {user_search} is not in the list") 


#  search method 2 try # index search with error handling

user_search = ""

while user_search != "exit":
    user_search = input(" m2 Search for a name in the list (exit to end) :")
    try:
        result = names.index(user_search)
        print(f"Yes {user_search} is in the list")
    except ValueError:
        print(f"{user_search} is not in the list")
