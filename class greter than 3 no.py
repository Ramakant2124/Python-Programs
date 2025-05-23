class GreatSmall:
    def check(self,a,b,c):
        if a>b and a>c:
            print(f"{a} is greater than {b} and {c}")
        elif a>b and a<c :
            print(f"{a} is greater than {b} smaller than {c}")
        elif a<b and a>c :
            print(f"{a} is greater than {c} smaller than {b}")
        elif a==b and a>c :
            print(f"{a} is equal to {b} smaller than {c}")
        elif a==b and a<c :
            print(f"{a} is equal to {b} smaller than {c}")
        elif a<c and a==b :
            print(f"{a} is greater tha {c} equal to {b}")
        elif a>c and a==b :
            print(f"{a} is greater tha {c} equal to {b}")
        if a<b and a<c:
            print(f"{a} is smaller than  {b} and {c}")    
            
        else:
            print("All is equal")
obj=GreatSmall()
e=int(input("Enter the number :"))
r=int(input("Enter the number :"))
s=int(input("Enter the number :"))
obj.check(e,r,s)
