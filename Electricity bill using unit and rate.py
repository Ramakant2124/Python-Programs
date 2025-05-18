unit=int(input("Enter number of units : "))
if unit<100 and unit>=0:
    print("0")
else:
    rate=int(input("Enter rate per unit : "))
    total=unit*rate
    print(total)
