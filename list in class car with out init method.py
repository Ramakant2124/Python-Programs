class Car:
    def f1(self,n,m,p):
        self.name=n
        self.model=m
        self.price=p

    def d1(self):
         print(f"Car name :{self.name}")
         print(f"Car Model :{self.model}")
         print(f"Car price :{self.price}")

c1=Car()
c1.f1("suzuki",2015,852000)
c1.d1()

c2=Car()
c2.f1("Toyta",2002,45200)
c1.d1()

car_list=[c1,c2]

for i in car_list:
    print(i.d1())

