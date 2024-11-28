import random

import code2flow

input_files = ['C:/Users/alanw/Documents/GitHub/Class/bogo.py']
output_file = 'C:/Users/alanw/Desktop/bogo_graph.dot'


code2flow.code2flow(input_files, output_file)


numberlist = [8,6,9,7]

random.shuffle(numberlist)
import code2flow

sorted  = False

while not sorted:
    # i want to check if, index 0 < i  = true then check index 1 vs index 2 
    # then if it gets to index  -2 < index -1 we know the list is sorted

    sorted = True 

    for i in range (len(numberlist)-1):
        if numberlist[i] > numberlist[i + 1]:
            # If any pair is out of order, the list is not sorted
            sorted = False
            break  # Exit the loop early
    
    if not sorted:
        print("Still not sorted:", numberlist)
        random.shuffle(numberlist)  # Shuffle again to try another arrangement

print("Sorted list:", numberlist)

