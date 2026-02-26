import math
# lambda r, h : (1/3) * pi * r^2 * h
cone_volume = lambda r, h: (1/3) * math.pi * (r**2) * h
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print(f"Volume of cone: {cone_volume(r, h):.2f}")