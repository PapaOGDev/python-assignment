first_number = int(input("Enter the first number"))
sign = input("Enter an operator")
second_number = int(input("Enter the second number"))
result = 0
if(sign == "+"):
    result = first_number + second_number
elif(sign == "-"):
    result = first_number - second_number
elif(sign == "*"):
    result = first_number * second_number
elif(sign == "/"):
    result = first_number / second_number
    
print(result)





