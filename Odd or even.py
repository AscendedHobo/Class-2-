# Program to validate user input

def validateNumber(incomingString):
    '''
       This function validates user's input

        params-in : incomingString  <str>
        params-out: validInput      <bool>
    '''


#    validDigits = ["0","1","2","3","4","5","6","7","8","9","."]

    validDigits = str([0, 1, 2, 3, 4, 5, 6, 7, "."])

    # check each character of the input string
    for character in incomingString:
        if character not in validDigits:
            return False

    return True


# ---------  MAIN PROCESSING STARTS ----------

# prod doesn;t store the user's value
while not validateNumber(input("Enter a number:")):
    print("Try again")


print("Goodbye")
