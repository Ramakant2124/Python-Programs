def prime(start,stop):
    a=0
    for r in range(start,stop):
        if r>1:
            for i in range(2,r):
                if r%i==0:
                    break
            else:
                a+=1
                print(r)
    print("total number of ",start,"and",stop,"are :",a)
start=int(input("Enter the number :"))
stop=int(input("Enter the number :"))

prime(start,stop)
