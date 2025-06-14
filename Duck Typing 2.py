class Sound:
    def sound(self):
        print("miwo ! miwo")
        print("-----------")

class Cow:
    def sound(self):
        print("Ambya ! Ambya")
        print("------------")

class Dog:
    def sound(self):
        print("bhaou ! bhaou")
        print("-------------")

class Hen:
    def sound(self):
        print("kuuuu ! kuuuu")
        print("-------------")
        
def getinfo(obj):
    obj.sound()
    

o=Sound()
o1=Cow()
o2=Dog()
o3=Hen()

getinfo(o)
getinfo(o1)
getinfo(o2)
getinfo(o3)
