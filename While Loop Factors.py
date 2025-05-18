num=int(input("Enter a number : "))
i=1
a=0
while i<=num:
    if num%i==0:
        print(i)
        a+=1
    i+=1
print("Total Factors :",a)
