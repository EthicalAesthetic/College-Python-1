# Define the tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in one line and the other half in the next line
mid = len(t1) // 2
print("First half of the tuple:", t1[:mid])
print("Second half of the tuple:", t1[mid:])

# b. Create a new tuple with only even numbers from t1
even_tuple = tuple([x for x in t1 if x % 2 == 0])
print("Tuple with even numbers:", even_tuple)

# c. Concatenate a new tuple t2 with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# d. Return maximum and minimum from the concatenated tuple
print("Maximum value:", max(t3))
print("Minimum value:", min(t3))
