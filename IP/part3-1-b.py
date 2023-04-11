num = int(input("Enter a number:"))
b = 0
for i in range(1,num+1):
    if i<=100: 
        a = i
        if a >= 0:
            b=b+i
            print(b)