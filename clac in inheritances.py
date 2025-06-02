
class Calc:
    def add(self,a,b):
        print("Add =",a+b)
    def sub(self,a,b):
        print("Sub =",a-b)
    def mul(self,a,b):
        print("Mul = ",a*b)
    def div(self,a,b):
        print("Div = ",a/b)
class Aclac(Calc):
    def squre(self,n):
        print("Squre=",n*n)
    def cube(self,n):
        print("Cube =",n*n*n)
ac=Aclac()
n=int(input("Enter your number :"))
ac.squre(5)
ac.cube(5)
a=int(input("Enter your  Frist number :"))
b=int(input("Enter your  Second number :"))
ac.add(a,b)
ac.sub(a,b)
ac.mul(a,b)
ac.div(a,b)
