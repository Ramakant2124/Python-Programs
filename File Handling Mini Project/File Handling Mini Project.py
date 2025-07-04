a=input("Enter a string : ")
vow=0
cons=0
ext=0
vow_li=[]
cons_li=[]
ext_li=[]

v="aeiouAEIOU"
for char in a:
    if (char>='a' and char<='z') or (char>='A' and char<='Z'):
        if char in v:
            vow+=1
            vow_li.append(char)
        else:
            cons+=1
            cons_li.append(char)
    else:
        ext+=1
        ext_li.append(char)
        
print("String :",a)
print("Number of Vowels in string",a,":",vow)
print("Number of Consonants in string",a,":",cons)
print("Neither Vowels nor Consonants in string",a,":",ext)
print()

#File Handling
f=open("C:\\Users\\LENOVO\\Desktop\\Vowels.txt","w")
cont=vow_li
f.writelines(cont)
f.close()

f=open("C:\\Users\\LENOVO\\Desktop\\Consonants.txt","w")
cont=cons_li
f.writelines(cont)
f.close()

f=open("C:\\Users\\LENOVO\\Desktop\\Extras.txt","w")
cont=ext_li
f.writelines(cont)
f.close()

#File Reading
f=open("C:\\Users\\LENOVO\\Desktop\\Vowels.txt")
print(f.read())
f.close()

f=open("C:\\Users\\LENOVO\\Desktop\\Consonants.txt")
print(f.read())
f.close()

f=open("C:\\Users\\LENOVO\\Desktop\\Extras.txt")
print(f.read())
f.close()
