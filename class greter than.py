class GreatSmall:
    def check(self,a,b):
        if a>b:
            print(f"{a} is greater than {b}")
        elif a<b:
            print(f"{a} is smaller than {b}")
        else:
            print(f"{a} is equal to {b}")
obj=GreatSmall()
e=int(input("Enter the number :"))
r=int(input("Enter the number :"))
obj.check(e,r)
