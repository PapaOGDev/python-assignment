first_score = float(input("Enter your first score: "))
second_score = float(input("Enter your second score: "))
third_score = float(input("Enter your third score: "))

average = (first_score + second_score + third_score)/3

if(average < 60):
    print("F")
elif(average>=60 and average < 70):
    print("D")
elif(average>=70 and average < 80):
    print("C")
elif(average>=80 and average < 90):
    print("B")
elif(average>=90 and average <=100):
    print("A")
