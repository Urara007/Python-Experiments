def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

n_terms = int(input("Enter number of terms: "))
print("Fibonacci series:")
for i in range(n_terms):
    print(recur_fibo(i), end=" ")