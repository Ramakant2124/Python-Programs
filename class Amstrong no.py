class Amstrong:
    def check(self,a):
        count=0
        b=str(a)
        for i in b:
            c=int(i)
            count+=c*c*c
        if count==a:
            print("Amstromg number ")
        else:
            print(" NOT Amstromg number ")
o=Amstrong()
num=int(input("Enter the number :"))
o.check(num)
               
