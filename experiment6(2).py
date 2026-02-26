n = int(input("Enter number of elements: "))
l = []
for i in range(n):
    l.append(float(input(f"Enter value {i+1}: ")))

numeric_tuple = tuple(l)
average = sum(numeric_tuple) / len(numeric_tuple)

print(f"Tuple: {numeric_tuple}")
print(f"Average: {average}")