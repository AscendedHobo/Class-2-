password = "letMeIn"

validPwd = False

Counter = 3

while validPwd != True or Counter > 3:

    if Counter == 0:
        print("Too many attempts program closing")
        break

    entered_pass = input("insert password:")
    Counter -= 1
    if entered_pass == password:
        validPwd = True
        print("Password accepted Welcome : User")

    else:
        print(f"{entered_pass} is incorrect please try again:")
        print(f"You have {Counter} attempts remaining")
