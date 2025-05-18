a=input("Enter a string : ")
vow=0
cons=0

ext=0
v="aeiouAEIOU"
for char in a:
    if (char>='a' and char<='z') or (char>='A' and char<='Z'):
        if char in v:
            vow+=1
        else:
            cons+=1
    else:
        ext+=1
print("String :",a)
print("Number of Vowels in string",a,":",vow)
print("Number of Consonants in string",a,":",cons)
print("Neither Vowels nor Consonants in string",a,":",ext)



'''
for i in range(len(a)):
    b=a[i]
    if b=='A' or b=='E' or b=='I' or b=='O' or b=='U' or b=='a' or b=='e' or b=='i' or b=='o' or b=='u':
        vow+=1
    else:
        cons+=1
print("String :",a)
print("Number of Vowels in string",a,":",vow)
print("Number of Consonants in string",a,":",cons)
'''

