while True:
    ch=int(input("\nEnter Choice:\n1.Add\t2.Sub\n3.Mul\t4.Div\n5.Exit : "))
    if ch==1:
        f=int(input("\nEnter First Number : "))
        s=int(input("Enter Second Number : "))
        print("Add =",f+s)
    elif ch==2:
        f=int(input("\nEnter First Number : "))
        s=int(input("Enter Second Number : "))
        print("Sub =",f-s)
    elif ch==3:
        f=int(input("\nEnter First Number : "))
        s=int(input("Enter Second Number : "))
        print("Mul =",f*s)
    elif ch==4:
        f=int(input("\nEnter First Number : "))
        s=int(input("Enter Second Number : "))
        print("Div =",f/s)
    elif ch==5:
        print("\nExiting.....")
        break
    else:
        print("\nInvalid Choice.....")
        
