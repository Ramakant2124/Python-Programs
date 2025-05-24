class Simpalint:
    def simple(self,p,r,t):
        si=(p*r*t)/100
        print ("simpal interest :",si)s
        
o=Simpalint()

p=int(input("Enter the principal Amount :"))
r=int(input("Enter the rate OF interest :"))
t=int(input("Enter the time in year :"))
o.simple(p,r,t)
