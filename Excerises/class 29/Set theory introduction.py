# # Quick intro to Python Sets
 
# A = {"a","b","c", "d", "e", "f"}
# B = { "a", "b", "x", "y"}
 
 
# print("A :", A)
# print("B :", B)
# print("A and B:", A & B)       # A intersection B
# print("A or  B:", A | B)       # A union B
 
# print("A or B but not both",  A ^ B )   # exclusive OR

# Quick intro to Python Sets and Set Theory

# Define sets
A = {"a", "b", "c", "d", "e", "f"}
B = {"a", "b", "x", "y"}

# Display sets
print("Set A:", A)
print("Set B:", B)

# Intersection (A ∩ B)
print("A and B (Intersection):", A & B)

# Union (A ∪ B)
print("A or B (Union):", A | B)

# Exclusive OR (Symmetric Difference: A ⊕ B)
print("A or B but not both (Symmetric Difference):", A ^ B)

# Difference (A - B and B - A)
print("Elements in A but not in B (A - B):", A - B)
print("Elements in B but not in A (B - A):", B - A)

# Superset and Subset relationships
print("Is A a superset of B?:", A.issuperset(B))
print("Is A a subset of B?:", A.issubset(B))
