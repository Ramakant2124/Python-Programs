rent=int(input("Enter rent : "))
depo=int(input("Enter Deposit : "))

unit=int(input("Enter number of units : "))
if unit<100 and unit>=0:
    total=rent+depo
    print("Cost for 1st Month:",total)
    print("Cost per Month :",rent)
    print("Cost for year :",rent*12)
else:
    rate=int(input("Enter rate per unit : "))
    total_bill=unit*rate
    print("Electricity Bill :",total_bill)
    total=rent+depo+total_bill
    print("Cost for 1st Month:",total)
    print("Cost per Month :",rent+total_bill)
    print("Cost for year :",(rent+total_bill)*12)


