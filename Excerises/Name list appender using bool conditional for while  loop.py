## creating the starting list of names
nameslist = ["alan", "ray" , "komal"]

# setting a bool for a checking if they are done adding
adding = True


## starting a while loop . using condition adding - if they still want to add names
##  
while adding == True:
    

### input first new names
    userinput =  (input("Type a name to add : ")).lower()

# append the  input to the list
    nameslist.append(userinput)

## ask if they want to add more names , if not then close while loop by changing condition to false

    keepgoing = (input("would you like to keep adding names?").lower())
    
    if keepgoing ==  "no":
        adding = False
       
    
## print the updated list
print(f"The updated list is {nameslist}")

