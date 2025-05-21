def prime(r):
    if r<=1:
        return False
    for i in range(2,r):
        if r%i==0:
            return False
    return True
num=int(input("Enter the number :"))
if prime(num):
    print("Prime number")
else:
    print("is not prime number :")
