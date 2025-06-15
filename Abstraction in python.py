from abc import ABC, abstractmethod
class RBI(ABC):
    def new_guidline(self):
        print("repo rate incressed by 0.7%")
        print("3rd party can be not saver corret ")
        print("kyc is mendatarynevery 2 year ")
        print("----------------------------------")

    @abstractmethod
    def interest_rate(self):
        pass

#r=RBI()
class HDFC(RBI):
    def interest_rate(self):
        print("intrset rate HDFC Bank id 2.2%")
        print("----------------------------------")
h=HDFC()
h.interest_rate()
h.new_guidline()
        
class ICICI(RBI):
    def interest_rate(self):
        print("\nintrset rate ICICI Bank id 5%")
        print("----------------------------------")
i=ICICI()
i.interest_rate()
i.new_guidline()
        
