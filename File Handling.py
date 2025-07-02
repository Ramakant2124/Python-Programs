print("\nTell Function:")
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.tell())#return cursors position
print(f.readline())
print(f.tell())#return cursors position
print(f.readline())
print(f.tell())#return cursors position
f.close()

print("\nSeek Function:")
f=open("C:\\Users\\Victus\\OneDrive\\Desktop\\daily python\\text.py")
print(f.seek(14))#return string from cursors position set by user
print(f.readline())
print(f.seek(21))#return string from cursors position set by user
print(f.readline())
print(f.seek(29))#return string from cursors position set by user
f.close()
