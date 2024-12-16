import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
######################################################################################################################################
# import csv as dataframe
dataframe = pd.read_csv("worldPopulation.csv")

# getting regions, using set to remove dupes, then making list for editing, and sorting
regionset =  set(dataframe["region"])
regionset = list(regionset)
regionset.sort()

# number list  based on indexin
tempindex = []
for i in range(len(regionset)):
    tempindex.append((i+1))

# merging those lists
merged = []
for i in range(len(regionset)):
    merged.append(tempindex[i])
    merged.append(regionset[i])

# Display choices for user 
for i in range(0, len(merged), 2):  # Increment by 2 for both lists to be printed together
    print(f"{merged[i]}-{merged[i+1]}")


userChoice = int(input("Please input the number of the Region population you would like to check : "))

# Get the region string, based on user input 
regiontocheck = merged[2 * userChoice - 1]


# list to store population values
population_list = []

# Iterate over the datrame rows and check the region column
for index, row in dataframe.iterrows():
    if row['region'] == regiontocheck:
        # Append the population value to the list
        population_list.append(int(row['value'].replace(',', '')))


# Calculate the sum of the list

totalpopulation = sum(population_list)

# Print the result
print(f"The total population for {regiontocheck} is {totalpopulation}")


worldpop = []

for index, row in dataframe.iterrows():
    # Remove commas and convert the population value to an integer
    population = int(row['value'].replace(',', ''))
    worldpop.append(population)



totalworld = sum(worldpop)

plt.pie([totalpopulation, totalworld], labels=[regiontocheck, "World Pop"], autopct='%1.1f%%')
plt.show()
