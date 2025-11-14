
father_age = int(input("Enter father's current age: "))
son_age = int(input("Enter son's current age : "))

number_of_years = father_age - 2 * son_age

years_difference = abs(number_of_years)

if number_of_years > 0:
    print(f"{years_difference} years ago, the father was twice as old as his son.")
elif number_of_years < 0:
    print(f"In {years_difference} years, the father will be twice as old as his son.")
else:
    print("Right now, the father is twice as old as his son!")

