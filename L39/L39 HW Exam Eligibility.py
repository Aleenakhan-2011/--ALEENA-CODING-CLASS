td = int(input("Enter total number of attendance days: "))
da = int(input("Enter number of days absent: "))

result = (td - da) / td * 100

print("Your attendance is: ", result)

if result < 75:
    print("You are not eligible for the exam.")
else:
    print("You are eligible for the exam.")