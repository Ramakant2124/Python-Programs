class Natural:
    def showSum(self,n):
        c=0
        for i in range(1,n+1):
            c+=i
        print("Total count :",c)
            
o=Natural()
n=int(input("Enter ending number : "))
o.showSum(n)
