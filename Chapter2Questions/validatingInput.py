count = 0;
while True:
    value = input("Enter a number")
    if value in ("1", "2"):
        print(f"number of time the wrong number was inputed: {count}")
        break;
    else:
        count +=1
