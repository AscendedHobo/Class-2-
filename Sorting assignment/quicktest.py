import random

# Function to generate a list of random numbers
def createlist(n_number):
    for i in range(0,n_number):                       ## range / length of the list from 0 to user input
        number_list.append(random.randint(0,1000))    # Random int appended to the list
        
    return number_list                       

# Function to choose a pivot (median of first, middle, last element)
def choose_pivot(number_list):
    first = number_list[0]
    middle = number_list[len(number_list) // 2]
    last = number_list[-1]
    
    # Find the median of first, middle, and last without sorting
    if (first <= middle <= last) or (last <= middle <= first):
        pivot = middle
    elif (middle <= first <= last) or (last <= first <= middle):
        pivot = first
    else:
        pivot = last
    
    return pivot


# QuickSort implementation
def quicksort(number_list):
    # Base case: list with one or zero elements is already sorted
    if len(number_list) <= 1:
        return number_list
    
    # Choose a pivot
    pivot = choose_pivot(number_list)
    
    # Partition the list into two sublists: less than pivot and greater than pivot
    # left = [x for x in number_list if x < pivot]
    # right = [x for x in number_list if x > pivot]
    # middle = [x for x in number_list if x == pivot]

    # Initialize empty lists for left, right, and middle partitions
    left = []
    right = []
    middle = []

    # Loop through the number_list and assign values to left, right, or middle
    for x in number_list:
        if x < pivot:
            left.append(x)     # Add to left if x is less than pivot
        elif x > pivot:
            right.append(x)    # Add to right if x is greater than pivot
        else:
            middle.append(x)   # Add to middle if x is equal to pivot

    
    # Recursively sort the left and right sublists and concatenate them with the middle
    return quicksort(left) + middle + quicksort(right)

# Main function to run the quicksort

# Create a random list of numbers

n_number = int(input("Insert list of numbers to be generated : "))    ## variable for length of list

number_list = []

createlist(n_number)
    
# Print the list before sorting
print("Before sorting:", number_list)

# Run the quicksort function and print the sorted list
sorted_list = quicksort(number_list)
print("After sorting:", sorted_list)
