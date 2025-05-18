charge=int(input("Per Month Gym cost : "))
cust=int(input("Number of customers : "))
daily=input("Is daily membership available(yes/no) : ")
if daily=="yes":
    total=charge*cust
    d=int(input("Enter daily charges : "))
    c=int(input("Enter number of daily customers : "))
    print("Daily Earning :",d*c)
    print("Total Cost per Month :",total)
    print("Total Cost per Year :",total*12)
    discount=int(input("Enter discount in percentage for month : "))
    dis=(discount/100)*charge*cust
    disc=(discount/100)*charge
    print("Discount amount per person :",disc)
    print("Total Discount amount :",dis)
    print("After discount amount for month :",total-dis)
    trainer=input("Do you need gym trainer?(y/n) : ")
    if trainer=="y":
        tr=int(input("Cost for trainer per month : "))
        print("Total Charge per month with trainer :",tr+charge)
else:
    total=charge*cust
    print("Total Cost per Month :",total)
    print("Total Cost per Year :",total*12)
    discount=int(input("Enter discount in percentage for month : "))
    dis=(discount/100)*charge*cust
    disc=(discount/100)*charge
    print("Discount amount per person :",disc)
    print("Total Discount amount :",dis)
    print("After discount amount for month :",total-dis)
    if trainer=="y":
        tr=int(input("Cost for trainer per month : "))
        print("Total Charge per month with trainer :",tr+charge)
