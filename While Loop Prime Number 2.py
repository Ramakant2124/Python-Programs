start=int(input("Enter Start : "))
j=start
stop=int(input("Enter Stop : "))
a=0
while start<stop:
    if start>1:
        i=2
        while i<start:
            if start%i==0:
                break
            i+=1
        else:
            a+=1
            print(start)
    start+=1
print("Total Prime numbers between",j,"and",stop,"are",a)    
