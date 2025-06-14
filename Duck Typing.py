class Honda:
    def Speed_max(self):
        print("Speed max in honda is 280 km")
    def transmission(self):
        print("transmission is honda automatic")
    def fule_type(self):
        print("fule_type is honda is desel")
        print("-------------------------------")

class Skoda:
    def Speed_max(self):
        print("Speed max in Skoda is 280 km")
    def transmission(self):
        print("transmission is Skoda manwel")
    def fule_type(self):
        print("fule_type is Skoda is petrol")
        print("-------------------------------")    
def get_info(obj):
    obj.Speed_max()
    obj.transmission()
    obj.fule_type()

honda_o=Honda()
skoda_o=Skoda()

get_info(honda_o)
get_info(skoda_o)
