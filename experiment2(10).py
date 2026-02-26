print("A  B | &  |  ^")
print("--------------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a}  {b} | {a & b}  {a | b}  {a ^ b}")