a=float(input("Enter 1st angle of triangle : "))
b=float(input("Enter 2nd angle of triangle : "))
c=float(input("Enter 3rd angle of triangle : "))
d=a+b+c
if d==180:
    print("Triangle is Valid")
    
    if a==b and a==c:
        print("Triangle is Equilateral")
    elif a==b or a==c or b==c:
        print("Triangle is Isoscale")
    else:
        print("Other type of triangle")
        
else:
    print("Triangle is invalid")
