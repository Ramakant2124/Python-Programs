unit=int(input("Enter number of units : "))
if unit<100 and unit>=0:
    print("0")
elif unit>=300:
    total=unit*20
    print(total)
elif unit>=200:
    total=unit*10
    print(total)
else:
    total=unit*5
    print(total)
