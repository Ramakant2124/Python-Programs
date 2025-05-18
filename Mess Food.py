charge=int(input("Enter Charger per month : "))
cust=int(input("Enter number of customers : "))
expense=int(input("Enter Expense per month : "))
total=(charge*cust)-expense
print("Earning per month :",total)
print("Earning per yearly :",total*12)
