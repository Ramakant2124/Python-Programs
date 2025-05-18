start=int(input("Enter Start : "))
stop=int(input("Enter Stop : "))
a=0
for g in range(start,stop):
    if g>1:
        for i in range(2,g):
            if g%i==0:
                break
        else:
            a+=1
            print(g)
print("Total Prime numbers between",start,"and",stop,"are",a)    
