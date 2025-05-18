start=int(input("Enter Start : "))
stop=int(input("Enter Stop : "))
a=0
for j in range(start,stop):
    if j%2==0:
        print(j)
        a+=1
print("Total Even numbers between",start,"and",stop,"are",a)
