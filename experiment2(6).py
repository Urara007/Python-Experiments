import math
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Area of the triangle: {area}")