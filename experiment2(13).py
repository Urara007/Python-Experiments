text = "Python Programming"
char = input("Enter character")
if char in text:
    print(f"'{char}' found in '{text}'")
else:
    print(f"'{char}' not found")