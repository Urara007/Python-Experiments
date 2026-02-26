sequence = (10, 20, 56, 78, 89)
num = int(input("Enter a number to search in the sequence: "))
if num in sequence:
    print(f"Yes, {num} is present in the sequence.")
else:
    print(f"No, {num} is not present in the sequence.")