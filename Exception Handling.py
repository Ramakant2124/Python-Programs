#Ex : 1
try :
    print("Try Block Start ")
    fn=int(input("Enter the Frist Number :"))
    sn=int(input("Enter the Second Number :"))
    ans=fn/sn
    print(ans)
    print("Try Block Ends")
except ZeroDivisionError as zde:
    print("please choose the  denometri value is non zero ")


#Ex : 2
try :
    print("\nTry Block Start ")
    fn=int(input("Enter the Frist Number :"))
    sn=int(input("Enter the Second Number :"))
    ans=fn/sn
    print(ans)
    print("Try Block Ends")
except ZeroDivisionError as zde:
    print("please choose the  denometri value is non zero ")
else :
    print("Division Successful ")


#Ex : 3
try :
    print("\nTry Block Start ")
    fn=int(input("Enter the Frist Number :"))
    sn=int(input("Enter the Second Number :"))
    ans=fn/sn
    print(ans)
    print("Try Block Ends")
except ValueError as ve :
    print("please Enter the integer number OR numeric whole number only " )
    
