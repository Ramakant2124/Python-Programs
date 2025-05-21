n=int(input("Enter Number : "))
g=str(n)
count=0
for i in g:
    d=int(i)
    e=d*d*d
    count+=e
if count==n:
    print("Yes")
else:
    print("No")
