class Circle:
    def area(self,r):
        r=3.14*r*r
        print("Area of Circle =",r)
o=Circle()
r=float(input("Enter Radius of Circle : "))
o.area(r)
