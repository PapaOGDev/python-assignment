a = int(input("Enter an integer value for a: "))
b = int(input("Enter an integer value for b: "))
c = int(input("Enter an integer value for c: "))

if(a > b and a > c):
    print(a)
else:
    if(b > a and b > c):
        print(b)
    else:
        print(c)
