total=0
i=1
while(i<=5):
    price=int(input("Enter Price : "))
    total+=price
    i+=1
print(total)
discount=total/2
print(discount)
gst=(discount*0.18)+discount
print(gst)
