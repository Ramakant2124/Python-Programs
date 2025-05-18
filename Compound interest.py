P=int(input("Enter Principle Amount : "))
R=int(input("Enter Rate of interest : "))
T=int(input("Enter Time in years : "))

A=P*(1+(R/100))**T
CI = A-P
print(A)
print(CI)
