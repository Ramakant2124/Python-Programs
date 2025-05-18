num=int(input("Enter a number : "))
i=2
if num>1:
    while i<num:
        if num%i==0:
            print("Not Prime number")
            break
        else:
            print("Prime number")
            break
        i+=1
else:
    print("Not Prime number")
