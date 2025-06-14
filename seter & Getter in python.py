class Emp:
    __eid=0
    __ename=""

    def setEid(self,i):
        self.__eid=i
    def getEid(self):
        return self.__eid
    def setEname(self,n):
        self.__ename=n
    def getEname(self):
        return self.__ename

e1=Emp()
e1.setEid(28)
e1.setEname("Ramakant")
print(e1.getEid())
print(e1.getEname())
