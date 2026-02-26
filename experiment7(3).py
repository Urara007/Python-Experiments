def print_upto_n(n, current=1):
    if current <= n:
        print(current, end=" ")
        print_upto_n(n, current + 1)

n_val = int(input("Enter n: "))
print_upto_n(n_val)