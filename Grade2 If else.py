a=int(input("Enter Marks of subject 1 : "))
b=int(input("Enter Marks of subject 2 : "))
c=int(input("Enter Marks of subject 3 : "))
d=int(input("Enter Marks of subject 4 : "))
e=int(input("Enter Marks of subject 5 : "))
f=a+b+c+d+e
print(f)
marks=(a+b+c+d+e)/5
print(marks)
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
