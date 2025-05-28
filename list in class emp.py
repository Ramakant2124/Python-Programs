class Emp:
    def __init__(self,i,n,s,d):
        self.eid=i
        self.ename=n
        self.sal=s
        self.dep=d
    def __str__(self):
        return f"EID={self.eid},EName={self.ename},salary={self.sal},Department={self.dep}"

e1=Emp(1,"ram",2500,"BCA")    
e2=Emp(2,"ramakant",26300,"MCA")   
e3=Emp(3,"rama",45200,"BBA")

emp_list=[e1,e2,e3]
for e in emp_list:
    print(e)
