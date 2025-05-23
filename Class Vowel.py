class Vowel:
    def check(self,string):
        countv=0
        countc=0
        vow="AEIOUaeiou"
        for i in string:
            if i in vow:
                countv+=1
            else:
                countc+=1
        print(f"Vowels : {countv}\nConsonants : {countc}")


v=Vowel()
st=input("Enter Your String : ")
v.check(st)
