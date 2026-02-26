num = int(input("Enter a number: "))
temp = num
sum_pow = 0
order = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** order
    temp //= 10

if num == sum_pow:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")