class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(C):
    pass
obj=D()

print(isinstance(obj,D))
print(isinstance(obj,C))
print(isinstance(obj,B))
print(isinstance(obj,A))
