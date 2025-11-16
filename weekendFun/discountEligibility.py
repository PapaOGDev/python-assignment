total_bill = float(input("Enter you total bill: "))
is_member = input("Are you a member?(yes/no): ")

if(total_bill >= 1000 and is_member == "yes"):
    discounted_price = total_bill - (total_bill * 0.1)
    print(f"Your discounted price is {discounted_price}")
elif(total_bill >= 1000 and is_member == "no"):
    discounted_price = total_bill - (total_bill * 0.05)
    print(f"Your discounted price is {discounted_price}")
else:
    print("No discount Print final amount and discount message.")
