class Student:
    rn=0
    name=""

    def setStudentinfo(self,r,n):
        self.rn=r
        self.name=n

    def getStudentinfo(self):
        print("get Student info method")
        print("rn=",self.rn)
        print("name=",self.name)

s2=Student()
s2.setStudentinfo(2,"ram")
s2.getStudentinfo()
        
