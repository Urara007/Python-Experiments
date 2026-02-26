n = int(input("How many values do you want to scan? "))
values = []

for i in range(n):
    val = int(input(f"Enter value {i+1} (0-3): "))
    values.append(val)

for i in range(4):
    print(f"Value {i} occurred {values.count(i)} times")