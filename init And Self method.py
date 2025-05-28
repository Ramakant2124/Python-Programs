class MyClass:
    def __init__(self):
        print("__init__ called ")
    def __str__(self):
        print("__str__ called")
        return " Return value pass str"
obj=MyClass()
print(obj)

class MyClass:
    rn=0
    name=""
    marks=0.0
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m

    def __str__(self):
        return f"rn={self.rn},name={self.name},marks={self.marks}"
o=MyClass(1,"ramakant",98)
print(o)

