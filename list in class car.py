class Car:
    def __init__(self,n,m,p):
        self.name=n
        self.model=m
        self.price=p

    def __str__(self):
        return f" Car name={self.name},Car Model={self.model}, Car price={self.price}"

c1=Car("suzuki",2017,85000)
c2=Car("Toyta",2015,45000)
c3= Car("Hundiai",2018,458151)

car_list=[c1,c2,c3]

for i in car_list:
    print(i)

