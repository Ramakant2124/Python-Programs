def ctof(c):
    f=(c*9/5)+32
    print(f)
def ftoc(f):
    c=(f-32)*5/9
    print(c)
c=float(input("Enter temperature in Celsius : "))
ctof(c)
f=float(input("Enter temperature in Fahrenheit : "))
ftoc(f)
