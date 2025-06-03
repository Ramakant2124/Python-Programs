class A:
    def m1(self):
        print("M1 is Class A called")
class B(A):
    def m1(self):
        print("M1 is Class B called")
        super().m1()
obj=B()
obj.m1()
