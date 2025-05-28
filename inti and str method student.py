class Student:
    rn=0
    name=""
    div=""
    add=""
    marks=0.0
    def __init__(self,r,n,d,ad,m):
        self.rn=r
        self.name=n
        self.div=d
        self.add=ad
        self.marks=m
        
    def __str__(self):
        return f"Rn={self.rn},name={self.name},div={self.div},addres={self.add},marks={self.marks}"
r=input("Enter  the Rool name :")
n=input("Enter  the name :")
d=input("Enter  the div :")
ad=input("Enter  the addres :")
m=input("Enter  the marks :")
o= Student(r,n,d,ad,m)
print(o)

