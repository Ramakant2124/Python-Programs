class A:
    pass
class B(A):
    pass
print(issubclass(A,B))
print(issubclass(B,A))
print(issubclass(A,object))
print(issubclass(B,object))
