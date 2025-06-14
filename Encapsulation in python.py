class Myclass:
    x=10   #public
    _y=20  #protected
    __z=30 #privet
    
myobj=Myclass()
print(myobj.x)  #10
print(myobj._y)  #20
print(myobj.__z) #Error
