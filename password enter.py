password = False
counter = 0
print(type(password))

if counter == 3:
    print("to many attempts system exiting")
    exit()


while password == False:
    attempt = input("Please enter password :")
    if password == attempt:
        print("Correct password welcome!")
    else:
        print("Incorrect password try again")
        counter += 1


    