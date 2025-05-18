a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print("A is Greater than B and C")
    elif a==c:
        print("A is Greater than B and Equals to C")
    else:
        print("A is Greater than B but Smaller than C")
elif a==b:
    if a>c:
        print("A is Equals to B and Greater than C")
    elif a==c:
        print("A is Equals to B and C")
    else:
        print("A is Equals to B but Smaller than C")
else:
    if a>c:
        print("A is Smaller than B but Greater than C")
    elif a==c:
        print("A is Smaller than B and Equals to C")
    else:
        print("A is Smaller than B and C")
