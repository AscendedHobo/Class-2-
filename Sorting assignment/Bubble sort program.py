##bubble sorting program

import random  

n_number = int(input("Insert list of numbers to be generated : "))    ## variable for length of list

number_list = []    ## empty list for appending to


#Function to create list with numbers between 0 , 1000
def createlist(n_number):
    for i in range(0,n_number):                       ## range / length of the list from 0 to user input
        number_list.append(random.randint(0,1000))    # Random int appended to the list
        
    return number_list                                # Returns the list for global scope use


##Compares index i-1 with i swaps them if needed also tracks if a change occured for the while loop to run again
def compare_and_swap():
    swapmade = 2                                                       ## Tracking varible to see compare against to see if a swap was made in any given pass
    loopnumber = 0                                                     ## Tracking varible to counts loops needed to sort 
    while swapmade >= 2:                                                                #### Condition for while loop is decteting if for loop ran 
        swapmade = 1
        for i in range(1,len(number_list)):                                             #  starting range 1, because if condition starts at i-1, this is to avoid out or range checks

            if number_list[i-1] > number_list[i]:                                       #  if index i-1 > index i , swap the vaules and add to the swap counter
                number_list[i-1], number_list[i]= number_list[i] , number_list[i-1]
                swapmade += 1
                loopnumber += 1
                print(number_list)                                                      ## can be removed but its nice to see it working in action

    if swapmade == 1:
        print(f"List sorted is {number_list} it took {loopnumber} loops to complete")

############### Main Processing ##############################

createlist(n_number)        ## function creates random list

print(f"List unsorted is {number_list} ")

compare_and_swap()    ## function compares and swaps till no swaps are made , then prints a final sorted list




## think swapmade can be a boolen ?

