marks=int(input("Enter your percentage : "))
if marks>100 or marks <0:
    print("Please enter Valid Marks")
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Pass")
else:
    print("Fail")
