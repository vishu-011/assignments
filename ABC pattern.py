#print pattern like
#A B C D E D C B A
#A B C D   D C B A
#A B         C B A
#A B           B A
#A               A
def pattern(n):
    for i in range(n): 
        for j in range(n - i):
            print(chr(65 + j), end=' ')
        for j in range(2 * i):
            print(' ', end=' ')
        for j in range(n - i - 1, -1, -1):
            print(chr(65 + j), end=' ')
        print()
n = int(input("Enter the number of rows: "))
pattern(n)
