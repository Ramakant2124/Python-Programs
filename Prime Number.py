num=int(input("Enter a number : "))
a=0
for i in range(2,num+1):
    if num%i==0:
        a+=1
if a==1:
    print("Prime Number")
else:
    print("Not a prime number")
