#read mode and its function
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.read())
f.close()
print()
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.readline())
f.close()
print()
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.readlines())
f.close()
print()

#use of tell() function
print("\nTell Function:")
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.tell())#return cursors position
print(f.readline())
print(f.tell())#return cursors position
print(f.readline())
print(f.tell())#return cursors position
f.close()

#use of seek() function
print("\nSeek Function:")
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.seek(14))#return string from cursors position set by user
print(f.readline())
print(f.seek(21))#return string from cursors position set by user
print(f.readline())
print(f.seek(29))#return string from cursors position set by user
f.close()

#use of strip()function
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
for i in f:
    print(i.strip())
f.close()

print()

#use of read mode with for loop
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
for i in f.read():
    print(i)
f.close()
print()
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
for i in f.readline():
    print(i)
f.close()
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
for i in f.readlines():
    print(i)
f.close()

# use OF Write Mode 
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text1.py","w")#create file mode : "x","a","w"
cont=['and\n','SBCV\n','12345']
#f.write("Hello Everyone!")
f.writelines(cont)
f.close()

f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text4.py","x")#create file mode : "x","a","w"
f.write("Hello Everyone!")
f.close()

#use of with function with  file handling 
with open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text3.py","w") as fh:
    fh.write("Harsh Here!")

file=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\Rowdy-Boys.jpg","rb") #'rb' mode is used to read binary files #png,jpg,jpeg,mp4,mp3
print(file.readline())
file.close()
