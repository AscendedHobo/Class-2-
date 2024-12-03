# Quick intro to Python Sets
 
A = {"a","b","c", "d", "e", "f"}
B = { "a", "b", "x", "y"}
 
 
print("A :", A)
print("B :", B)
print("A and B:", A & B)       # A intersection B
print("A or  B:", A | B)       # A union B
 
print("A or B but not both",  A ^ B )   # exclusive OR