P=int(input("Enter Principle Amount : "))
R=int(input("Enter Rate of interest : "))
T=int(input("Enter Time in years : "))
SI=(P*R*T)/100
print("Simple Interest :",SI)
total=P+SI
print("Total Payable :",total)
M=T*12
print("Total Monthss :",M)
EMI=total/M
print("EMI :",EMI)
