class Bank:
    __aname=""
    __anum=0
    __abla=0.0

    def __init__(self,name,num,bla):
        self.__aname=name
        self.__anum=num
        self.__abla=bla

    def setAname(self,name):
         self.__aname=name
    def getAname(self):
         return self.__aname

    def getInfo(self):
         print("\nAccount Name :",self.__aname)
         print("\nAccount Number :",self.__anum)
         print("\nAccount Blances :",self.__abla)

    def depositBal(self,bal):
        if bal<=0:
            print("please Enter Value greter than 0")
        else:
            self.__abla+=bal
            print("\nDeposit Succesful Amount ")
    def WithdrawBal(self,bal):
        if bal>self.__abla:
            print("not enough balance in your Account")
        else:
            self.__abla-=bal
            print("\nWithdraw Succesful Amount ")
            
    def checkBal(self):
         print("\nAcount Blances :",self.__abla)

b1=Bank("abc",12455351822,50000)
b1.getInfo()

b1.setAname("EFG")
print(b1.getAname())
b1.getInfo()

b1.depositBal(5000)
b1.checkBal()

b1.WithdrawBal(2000)
b1.checkBal()
