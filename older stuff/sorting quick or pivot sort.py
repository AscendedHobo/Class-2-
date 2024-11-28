number_list = [4, 6, 9, 8, 2]

pivot = number_list[-1]  # pivot is the last element, which is 2

L = 0  # Left pointer
R = len(number_list) - 2  # Right pointer starts just before the pivot (index 3)

while L <= R:
    # Move L to the right until it finds an element greater than the pivot
    while number_list[L] < pivot:
        L += 1

    # Move R to the left until it finds an element smaller than the pivot
    while number_list[R] > pivot:
        R -= 1
