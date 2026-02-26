n = int(input("Enter number of test cases: "))

for i in range(n):
    try:
        # Taking space separated input
        a, b = input("Enter a and b: ").split()
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")