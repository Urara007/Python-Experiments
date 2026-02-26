import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4*a*c
if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Real roots: {root1} and {root2}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-d) / (2*a)
    print(f"Imaginary roots: {real_part} + {imag_part}j and {real_part} - {imag_part}j")