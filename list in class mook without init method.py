class Book:
    def f1 (self,bn,bi,bp):
        self.bname=bn
        self.bid=bi
        self.bprice=bp

    def d2(self):
        print(f"Book name ={self.bname}")
        print(f"BooK id ={self.bid}")
        print(f"Book price={self.bprice}")

b1=Book()
b2=Book()

b1.f1("python",1,500)
b2.f1("django",2,800)

book_list=[b1,b2]

for i in book_list:
    i.d2()
