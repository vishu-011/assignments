i=int(input("enter no. of rows"))
for row in range(1,i+1):
    ASCII=65
    for col in range(row):
        print(chr(ASCII),end=" ")
        ASCII+=1
    print()