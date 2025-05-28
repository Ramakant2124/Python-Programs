class Book:
    def __init__(self,bi,bn,bp):
        self.bid=bi
        self.bname=bn
        self.bprice=bp

    def __str__(self):
        return f"BooK ID ={self.bid},Book name={self.bname},Book price={self.bprice}"


b1=Book(1,"Python",500)
b2=Book(2,"django",700)
b3=Book(3,"React",800)

Book_list=[b1,b2,b3]

for i  in Book_list:
    print(i)
         
