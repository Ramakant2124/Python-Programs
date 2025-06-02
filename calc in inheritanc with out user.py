
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
ac.squre(5)
ac.cube(5)
ac.add(10,20)
ac.sub(10,20)
ac.mul(10,20)
ac.div(10,20)
