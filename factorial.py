def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r
n = int(input("Enter a number to calculate its factorial: "))
print(factorial(n))