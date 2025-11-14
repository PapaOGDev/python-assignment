age = float(input("Enter your age: "))
max_heart_rate = 220 - age

target_lower = max_heart_rate * 0.50
target_upper = max_heart_rate * 0.85

print(f"Your maximum heart rate is {max_heart_rate} and the range is {target_lower} - {target_upper}")
