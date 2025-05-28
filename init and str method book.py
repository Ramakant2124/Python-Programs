

class Book:
    bn=""
    ba=""
    bp=""
    bprice=0.0
    def __init__(self,n,a,p,bp):
        self.bn=n
        self.ba=a
        self.bp=p
        self.bprice=bp
        
    def __str__(self):
        return f"book name ={self.bn},book author={self.ba},book publisher={self.bp},book price ={self.bprice}"
n=input("Enter  the book name :")
a=input("Enter  the book author :")
p=input("Enter  the book publisher :")
bp=input("Enter  the book price :")

o= Book(n,a,p,bp)
print(o)
