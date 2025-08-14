def pn(n):
    for i in range(2, int(n**0.5) + 1):
        if n == 1:
            print("1 is neither prime nor composite.")
            break
        else:
            if n % i == 0:
                print(n,"is not a prime number.")
                break
    else:
        print(n,"is a prime number.")
n=int(input("Enter a number to check if it is prime: "))
pn(n)