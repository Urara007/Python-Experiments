text = input("Enter a string: ")
count = 0
capitals = []

for char in text:
    if char.isupper():
        count += 1
        capitals.append(char)

print(f"Number of capital letters: {count}")
print(f"Capital letters found: {' '.join(capitals)}")