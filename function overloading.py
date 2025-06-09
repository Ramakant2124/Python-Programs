from multipledispatch import dispatch
@dispatch(int,int,int)
def add(a,b,c):
    ans=a+b+c
    print(ans)

@dispatch(int,int)
def add(a,b):
    ans=a+b
    print(ans)

add(10,20,30)
add(10,20)
