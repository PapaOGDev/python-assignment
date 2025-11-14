first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

add = first_number + second_number + third_number
average = add / 3
product = first_number * second_number * third_number

largest_number = first_number
smallest_number = first_number

if second_number > largest_number:
    largest_number = second_number
if third_number > largest_number:
    largest_number = third_number

if second_number < smallest_number:
    smallest_number = second_number
if third_number < smallest_number:
    smallest_number = third_number

print(f"The sum is {add}, the average is {average}, the product is {product}, the largest number is {largest_number}, and the smallest number is {smallest_number}.")

