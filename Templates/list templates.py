# Python List Reference Template

# 1. Creating Lists
example_list = [1, 2, 3, 4, 5]
nested_list = [[1, 2], [3, 4]]

print("Example List:", example_list)
print("Nested List:", nested_list)

# 2. Common Methods
example_list.append(6)  # Adds an item to the end
print("After append(6):", example_list)

example_list.insert(2, 99)  # Inserts 99 at index 2
print("After insert(2, 99):", example_list)

example_list.remove(99)  # Removes the first occurrence of 99
print("After remove(99):", example_list)

example_list.pop()  # Removes and returns the last item
print("After pop():", example_list)

example_list.reverse()  # Reverses the list in place
print("After reverse():", example_list)

example_list.sort()  # Sorts the list in ascending order
print("After sort():", example_list)

# 3. List Comprehensions
squared = [x**2 for x in example_list]
print("List Comprehension (squared values):", squared)

# 4. Slicing
print("Full list:", example_list[:])  # Full list
print("First three elements:", example_list[:3])  # Up to index 3 (exclusive)
print("Last three elements:", example_list[-3:])  # Last 3 elements
print("Step slicing (every other element):", example_list[::2])

# 5. Splitting a List
split_list = example_list[:3], example_list[3:]  # Splitting into two parts
print("Split list into two:", split_list)

# 6. Merging Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2  # Concatenating two lists
print("Merged List:", merged_list)

list1.extend(list2)  # Extending list1 with elements from list2
print("List1 after extend:", list1)

# 7. Other Useful Methods
print("Index of element '2':", example_list.index(2))  # Index of first occurrence of 2
print("Count of element '2':", example_list.count(2))  # Count occurrences of 2

# 8. Looping Through Lists
print("Looping through list:")
for item in example_list:
    print(item)

# 9. Clearing a List
example_list.clear()
print("After clear():", example_list)


# Start, Stop, Step Examples in Slicing

# Example list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original List:", my_list)

# 1. Default Slicing
print("\n1. Default Slicing")
print("Full list (my_list[:]):", my_list[:])

# 2. Start and Stop
print("\n2. Start and Stop")
print("Slice from index 2 to 6 (my_list[2:6]):", my_list[2:6])

# 3. Step
print("\n3. Step")
print("Every second element (my_list[::2]):", my_list[::2])
print("Every third element (my_list[::3]):", my_list[::3])

# 4. Reverse with Negative Step
print("\n4. Reverse with Negative Step")
print("Full reverse (my_list[::-1]):", my_list[::-1])
print("Reverse every second element (my_list[::-2]):", my_list[::-2])

# 5. Combining Start, Stop, and Step
print("\n5. Combining Start, Stop, and Step")
print("From index 1 to 8, every second element (my_list[1:8:2]):", my_list[1:8:2])
print("From index 8 to 1 in reverse, step -2 (my_list[8:1:-2]):", my_list[8:1:-2])
print("From index 5 to the end, step 1 (my_list[5:]):", my_list[5:])
print("From start to index 5, step 1 (my_list[:5]):", my_list[:5])

# 6. Edge Cases
print("\n6. Edge Cases")
print("Empty slice (my_list[10:]):", my_list[10:])  # Stop beyond the end
print("Empty slice (my_list[:0]):", my_list[:0])  # Stop at index 0
print("Start beyond end (my_list[10:15]):", my_list[10:15])
