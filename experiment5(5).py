text = input("Enter string: ").upper()
unique_chars = sorted(set(text))
for char in unique_chars:
    if char.isalpha():
        print(f"{text.count(char)}{char}")