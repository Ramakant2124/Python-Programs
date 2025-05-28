class Emp:
    eid=0.0
    ename=""
    dept=""
    sla=0.0
    def __init__(self,i,n,d,s):
        self.eid=i
        self.ename=n
        self.dept=d
        self.sla=s

    def __str__(self):
        return f"Eid={self.eid},Ename={self.ename},Department={self.dept},slary={self.sla}"
i=input("Enter the eid :")    
n=input("Enter the ename :")
d=input("Enter the Deparment:")
s=input("Enter the slary :")

o=Emp(i,n,d,s)
print(o)
