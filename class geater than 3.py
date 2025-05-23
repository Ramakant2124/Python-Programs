class GeaterSamller:
    def check(self,a,b,c):
        if a==b and b==c:
            print("All number are same")
        elif a>b and b>c:
            print("a is geater than")
        elif b>c:
            print("b is geater than")
        else:
            print("c is geater than")
obj=GeaterSamller()    
e=int(input("Enter the number :"))
r=int(input("Enter the number :"))
s=int(input("Enter the number :"))
obj.check(e,r,s)
    
    
    
