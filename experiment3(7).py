day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    max_days = 31
elif month in [4, 6, 9, 11]:
    max_days = 30
elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    max_days = 29
else:
    max_days = 28

if day < max_days:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print(f"Next Date: day={day} month={month} year={year}")