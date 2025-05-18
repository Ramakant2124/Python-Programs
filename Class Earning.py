fee=int(input("Enter average fee per student(YEARLY) : "))
student=int(input("Enter number of students : "))
expense=int(input("Enter expenses per month(ALL) : "))
total_cost=fee*student
monthly_cost=total_cost/12
monthly_earn=monthly_cost-expense
total_earn=monthly_earn*12
print("Total Fee :",total_cost)
print("Average Monthly Fee :",monthly_cost)
print("Monthly Expenses :",expense)
print("Monthly Earning :",monthly_earn)
print("Total Earning :",total_earn)
