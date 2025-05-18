num=int(input("Enter a number of terms : "))
a=0
b=1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
    
'''
i=0
while i<num:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1
'''
