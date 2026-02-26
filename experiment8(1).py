# Create and add names to the file
names_to_add = ["Aman", "Ojas", "Binay", "Ishita", "Umang", "Zoya"]
with open("name.txt", "w") as f:
    for name in names_to_add:
        f.write(name + "\n")

# Analysis
with open("name.txt", "r") as f:
    names = [line.strip() for line in f.readlines()]

# a. Count no of names
print(f"Total names: {len(names)}")

# b. Count names starting with vowel
vowels = "AEIOUaeiou"
vowel_names = [n for n in names if n[0] in vowels]
print(f"Names starting with a vowel: {len(vowel_names)}")

# c. Find longest name
longest = max(names, key=len)
print(f"Longest name: {longest}")