validDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "."]

thestring = input("Enter numbers: ")

validinput = True

for character in thestring:
    if character in validDigits:
        validinput = True

    else:
        validinput = False
        print("Invalid Character Detected")
        break

print(f"Input was {validinput}")


mynumber = int(input())

if mynumber is int:
    print("valid input")
else:
    print("invalid input")
