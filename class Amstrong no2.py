class Amstrong:
    def check(self,n):
        a=n
        s=0
        while(a>0):
            rem=a%10
            c=rem**3
            s=s+c
            a=a//10
        if s==n:
              print("Amstromg number ")
        else:
              print(" NOT Amstromg number ")
o=Amstrong()
num=int(input("Enter the number :"))
o.check(num)              
              
