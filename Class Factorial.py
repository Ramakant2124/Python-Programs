class Factorial:
    def check(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print("Factorial of",n,"is",fact)
num=int(input("Enter a number : "))
fact=Factorial()
fact.check(num)
