S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

print(f"Set 1: {S1}")
print(f"Set 2: {S2}")

# Union (|)
print(f"Union (All colors): {S1 | S2}")

# Intersection (&)
print(f"Intersection (Common colors): {S1 & S2}")

# Difference (-)
print(f"Difference (S1 - S2): {S1 - S2}")

# Symmetric Difference (^) - elements in either S1 or S2, but not both
print(f"Symmetric Difference: {S1 ^ S2}")