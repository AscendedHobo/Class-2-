# Temp converter

# ask if starting vaule is C or F
choice_type = input("Is your Starting Value in C or F? :").lower()

while choice_type != "c" and choice_type != "f":
    print("Invalid option please Type C or F :")
    choice_type = input("Is your Starting Value in C or F? :").lower()

# now we ask them for the number value
choice_number = (input("Please enter the Value : "))

while type(choice_number) != float:
    print("Invalid option please Type a number ")
    choice_number = float(input("Please enter the Value : "))

###

answer = (choice_number * 9/5) + \
    32 if choice_number == "f" else (choice_number - 32) * 5/9

print(f"{choice_number} converted is {answer} ")


# print(f"{choice_number} converted is {answer} ")
#
# answer = if choice_type == "c":
#            (choice_number * 9/5) +32
#        else:
#            (choice_number - 32) *5/9


# if choice_number == "c":
#    print
# try:
#    print(f"Converted number is {F_to_C}")
# finally:
#    print(f"Converted number is {C_to_F}")
