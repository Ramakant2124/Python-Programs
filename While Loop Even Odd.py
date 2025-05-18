start=int(input("Enter Start : "))
stop=int(input("Enter Stop : "))
a=0
i=start
while i<stop:
    if i%2==0:
        print(i)
        a+=1
        i+=1
    else:
        i+=1
print("Even Numbers between",start,"and",stop,":",a)
