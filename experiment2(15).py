text = "Python Programming"
char = input("Enter a character to search for: ")
if char in text:
    print(f"Yes, '{char}' was found in the string.")
else:
    print(f"No, '{char}' was not found in the string.")