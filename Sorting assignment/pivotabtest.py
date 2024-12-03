
import random  

#n_number = int(input("Insert list of numbers to be generated : "))    ## variable for length of list
n_number = 5
number_list = []    ## empty list for appending to

#Function to create list with numbers between 0 , 1000
def createlist(n_number):
    for i in range(0,n_number):                       ## range / length of the list from 0 to user input
        number_list.append(random.randint(0,1000))    # Random int appended to the list
        
    return number_list                                # Returns the list for global scope use

#createlist()

number_list = [4, 6, 9, 8, 2]

# get first , middle and last numbers in index

## this function creates a pivot number based on the median of the first middle and last index of the list
def choosepiv():
    # get first , middle and last index locatoin in list
    indices = [0, (len(number_list)-1)//2, len(number_list)-1]
    
    # Create a tuple list, of to store vaule + index together in the return
    sortlist = []
    for i in indices:
        sortlist.append((number_list[i], i))  # uses the vaule in indices list, to get correct vaule from numberlist , and append that vaule and index number togeter
    
   
    # quick manual sort of the list of 3 items
    if sortlist[0][0] > sortlist[1][0]:
        sortlist[0], sortlist[1] = sortlist[1], sortlist[0]
    if sortlist[1][0] > sortlist[2][0]:
        sortlist[1], sortlist[2] = sortlist[2], sortlist[1]
    if sortlist[0][0] > sortlist[1][0]:
        sortlist[0], sortlist[1] = sortlist[1], sortlist[0]

    # return a sorted list with vaule and index location
    return sortlist[1]





# left item is bigger than pivot
# right item is smaller than pivot
##stop when index of Left item, is greater than item from right
# then swap left item with pivot 

def quicksort():
   
    # check to see if the len of the list is 0 or 1 , as this would mean its already sorted and doesnt need altering
    if len(number_list) <= 1:
        return number_list ## this will end the function

    pivot_value, pivot_index = choosepiv()  # creates these variables from the choosepiv function
    number_list[pivot_index], number_list[-1] = number_list[-1], number_list[pivot_index]


    left = 0
    right = len(number_list) - 2  # Start one before the pivot at the end

    while left <= right:  ## condition to be meet to swap the pivot into its correct end point

        while number_list[left] < pivot_value:  #  this searchs the indexs left to right, until left is larger than pivot
            left += 1

        while number_list[right] > pivot_value: # like the above but right to left, and stops when right is smaler than pivot
            right -= 1

        if left <= right:      # checks the vaules, and swaps them in the NUMBER LIST if needed
            number_list[left], number_list[right] = number_list[right], number_list[left]
            left += 1
            right -= 1
    

    # once the while loop condition is no longer true, vaule of left is greater than vaule of right
    # we swap the location of left and pivot, this places pivot in its final correct location
    number_list[left], number_list[-1] = number_list[-1], number_list[left]

    
    # Recursively sort the left and right sublists
    left_sorted = quicksort(number_list[:left])  # Sort the left part

    right_sorted = quicksort(number_list[left + 1:])  # Sort the right part

    # Combine the left, pivot, and right parts
    return left_sorted + [number_list[left]] + right_sorted

#########  Main Processing #######################

print(number_list)

sorted_list = quicksort(number_list)

print("After sorting:", sorted_list)

