class Compoundint:
    def compound(self,p,r,t):
        ta=p*(1 + r/100)**t
        print(("Total ampount :",ta))
        ci=ta-p
        print("Comound interest :",ci)
        



o=Compoundint()
p=float(input("Enter the principal Amount :"))
r=float(input("Enter the rate OF interest :"))
t=float(input("Enter the time in year :"))
o.compound(p,r,t)
