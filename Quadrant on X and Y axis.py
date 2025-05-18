x=int(input("Enter X-axis Point : "))
y=int(input("Enter Y-axis Point : "))

if x==0 and y==0:
    print("At Origin")
elif x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>=0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x>=0 and y<0:
    print("4th Quadrant")
