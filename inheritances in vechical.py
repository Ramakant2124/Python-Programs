class Vehicle:
    def fi(self,n,m,p):
        self.name=n
        self.model=m
        self.price=p
    def d1(self):
        return f"V Name :{self.name},V Model :{self.model},V Price :{self.price}"
class Owner(Vehicle):
    def odtials(self,na,ph):
        self.name=na
        self.phonen=ph
    def d2(self):
        return f"Owner Name :{self.name},Phone Number :{self.phonen}"
o=Owner()
na=input("Enter your owner name :")
ph=int(input("Enter your Phone number :"))
o.odtials(na,ph)
print(o.d2())
n=input("Enter your car name :")
m=int(input("Enter your Model Number :"))
p=int(input("Enter your car Price :"))
o.fi(n,m,p)
print(o.d1())


