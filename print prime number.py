def  print_prime(num):
    if num < 2:
        print("No prime numbers less than 2")
    else:
        print("Prime numbers up to", num, "are:")
        for i in range(2, num + 1):
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i)
num = int(input("Enter a number till which we have to check prime: "))
print_prime(num)
              