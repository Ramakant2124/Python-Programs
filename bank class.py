class Bank:
    name="Ramakant"
    amount=300000
    def deposit(self,a):
        self.a=a
        self.amount+=self.a
        print("Total amount :",self.amount)
    def withdraw(self,a):
        self.a=a
        self.amount-=self.a
        print("Total amount :",self.amount)
    def get(self):
        print("name :",self.name)
        print("Total amount :",self.amount)
b1=Bank()
b1.get()
b1.deposit(1500)
b1.withdraw(2000)
b1.get()
