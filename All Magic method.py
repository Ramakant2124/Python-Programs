class ABC:
    def __init__(self,a):
        self.a=a
        
    def __add__(self,other):
        return self.a+other.a

    def __sub__(self,other):
        return self.a-other.a

    def __mul__(self,other):
        return self.a*other.a
    
    def __truediv__(self,other):
        return self.a/other.a

    def __mod__(self,other):
        return self.a%other.a

    def __floordiv__(self,other):
        return self.a//other.a

    def __pow__(self,other):
        return self.a**other.a

    #def __lshift__(self,other):
    #    return self.a<<other.a

    #def __rshift__(self,other):
    #    return self.a>>other.a

    def __and__(self,other):
        return self.a&other.a

    def __or__(self,other):
        return self.a|other.a

    def __xor__(self,other):
        return self.a^other.a

    #def __matmul__(self,other):
    #    return self.a@other.a

a1=ABC(8)
b1=ABC(2)

print("+  :",a1+b1)
print("-  :",a1-b1)
print("*  :",a1*b1)
print("/  :",a1/b1)
print("%  :",a1%b1)
print("// :",a1//b1)
print("** :",a1**b1)
print("&  :",a1&b1)
print("|  :",a1|b1)
print("^  :",a1^b1)

#print("<< :",a1<<b1)
#print(">> :",a1>>b1)
#print("@ :",a1@b1)
