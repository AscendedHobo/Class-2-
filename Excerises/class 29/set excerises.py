#############################################################################################################################
# 1. Define a set, dogs, with five dog breeds.
# 2. Check if “tabby” is a member of the set, printing a suitable message as
# appropriate.
# 3. Using a list add another 3 dog breeds to your set.
# 4. Print the set and its length.

# dogs = {"Labrador", "Bulldog", "Beagle", "Poodle", "German Shepherd"}
# print("Dog breeds:", dogs)

# userinput = ""

# while userinput !=  "e":
        

#     userinput = input("Insert a dog name to add to the list [e] to exit")
#     if userinput  !=  "e":
#         if userinput in dogs:
#             print(f"{userinput} is in the already set pick another name")
            
#         else:
#             print(f"{userinput} is not in the set it has been added")
#             dogs.add(userinput)

#         print(f"the set currently  contains {dogs}")



# print(f"updated set is : {dogs}")
# print(f"Length of set : {len(dogs)}")

# #############################################################################################################################

# # # 1. Define a set of working days: Monday to Friday
# # # 2. Define a set of non-working days, Saturday and Sunday
# # # 3. Use set union to create a set representing a whole week


# # Set of working days (Monday to Friday)
# working_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}

# # Set of non-working days (Saturday and Sunday)
# non_working_days = {"Saturday", "Sunday"}

# wholeweek = working_days | non_working_days

# print(wholeweek)

# #############################################################################################################################


# 1. Define a set of months for each of the four seasons.
# 2. Define a set of academic months, typically September to June.
# 3. Print the union and intersection of the seasons and academic sets.


# spring = {"March", "April", "May"}
# summer = {"June", "July", "August"}
# autumn = {"September", "October", "November"}
# winter = {"December", "January", "February"}

# academic_months = {"September", "October", "November", "December", "January", "February", "March", "April", "May", "June"}

# autumninter  = autumn & academic_months
# winterinter  = winter & academic_months
# summerinter =  summer & academic_months
# springinter  = spring & academic_months

# print(f"spring intersections {springinter} \n summer intersection {summerinter} \n autumn intersection {autumninter}\n winter intersection {winterinter}")

# # #############################################################################################################################

# Consider the maths and English sets shown. Using Python answer the following.

# 1. How many students are there in total?
# 2. Which students took both maths and English?
# 3. Which students took maths only?
# 4. Which students took English only?

maths = {"Mark", "Jane", "Patrick", "Jenny", "Rahoul"}
english = {"Rahoul", "Jane", "Simon", "Amber", "Patrick", "Jo", "Shelly"}

print(f"Maths students : {maths}")
print(f"English students : {english}")
# 1. How many students are there in total?
print(f"The total number of students are {len( maths | english)}")

# 2. Which students took both maths and English?
print(f"The students that took maths and english are  {maths & english}")

# 3. Which students took maths only?
print(f"The students that took maths but not english   {maths - english}")

# 4. Which students took English only?
print(f"The students that took maths but not english   {english - maths}")

##########################################################################################################







#notes while learning  

# fruits = set(("apple", "banana", "pear", "tomato"))
# # print(fruits)

# listabc = {"a","b","c",5,6,8,7,5}

# listcba = {"c" , "b" , "a", "e"}

# combined  = listabc | listcba

# print(combined)

# while "a"  in listabc:
#     print("a" in listabc)
#     print("a" not in listabc)

# print(len(modes_of_transport))
# for mode in modes_of_transport:
#     print(mode)

# print( modes_of_transport)

# modes_of_transport.remove("cars")
# modes_of_transport.discard("cars")


# modes_of_transport = {"car", "bicycle", "train", "airplane", "boat"}


# modes_of_transport.update( "bus" , ["listbus","list train"] , {"set buss"} )


# modes_of_transport = {"car", "bicycle", "train", "airplane", "boat"}
# print( modes_of_transport)

# poppedlist = []
# for mode in range(0, len(modes_of_transport)):
#     poppedlist.append(modes_of_transport.pop())

# print(poppedlist)

# modes_of_transport.clear
# name =  ["alan", "rajul"]
# print(name)
# name.clear()
# print(name)

# name = "alan"
# name.clear()   doesnt work because strings are immutable
# print(name)
