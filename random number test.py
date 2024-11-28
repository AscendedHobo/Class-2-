import random

times = 0

while times < 5:
    numberlist = []
    times += 1

    # Generate a list of random integers
    for i in range(1, 99):  # Creates 98 numbers
        numberlist.append(random.randint(30, 50))  # Random ints between 30 and 50

    # Calculate the mean
    total = sum(numberlist)
    mean = total / len(numberlist)
    print(f"The mean is {mean}")

    # Calculate the median
    numberlist.sort()

    if len(numberlist) % 2 == 0:
        index1 = (len(numberlist) // 2) - 1
        index2 = len(numberlist) // 2
        median = (numberlist[index1] + numberlist[index2]) / 2
    else:
        median = numberlist[len(numberlist) // 2]

    print(f"The median is {median}")

    # Calculate the mode
    mode_lists = []
    unique_numbers = set(numberlist)

    for num in unique_numbers:
        listname = []
        count = numberlist.count(num)
        for _ in range(count):
            listname.append(num)
        mode_lists.append(listname)

    # Find the largest list (most frequent number)
    mode_lists.sort(key=len, reverse=True)
    largest_mode_list = mode_lists[0]  # The most frequent number's list

    print(f"The mode is {largest_mode_list[0]} with frequency {len(largest_mode_list)}")
