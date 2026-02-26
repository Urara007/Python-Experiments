n = int(input("How many fruits in each set? "))

print("Enter fruits for Set 1:")
s1 = {input(f"Fruit {i+1}: ") for i in range(n)}

print("Enter fruits for Set 2:")
s2 = {input(f"Fruit {i+1}: ") for i in range(n)}

# a. Intersection
print(f"Fruits in both sets: {s1.intersection(s2)}")

# b. Difference
print(f"Fruits only in s1: {s1.difference(s2)}")

# c. Union Count
print(f"Total count of unique fruits from both: {len(s1.union(s2))}")