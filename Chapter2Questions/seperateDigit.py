number = int(input("Enter a 5-digit number"))
first_number = int(number/10000)
second_number = int(number/1000) % 10
third_number = int(number/100) % 10
fourth_number = int(number/10) % 10
fifth_number = number % 10
print(f"{first_number}  {second_number}  {third_number}  {fourth_number}  {fifth_number}")

