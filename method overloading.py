from multipledispatch import dispatch

class Myclass:
    @dispatch(float,float)
    def Add(self,a,b):
        ans=a+b
        print(ans)
        
    @dispatch(int,int,int)
    def Add(self,a,b,c):
        ans=a+b+c
        print(ans)
myobj=Myclass()
myobj.Add(10.6,20.5)
myobj.Add(10,20,30)
