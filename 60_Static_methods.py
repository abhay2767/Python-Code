#Static methods are those methods whose Neither belongs to Instance nor Class.
#Mean we use Static methods when we don't required need of Class and Instance.
class Calc:
    def __init__(self,num): #Constructor
        self.num = num

    def addToNum(self,n): #This is an Instance method
        self.num = self.num+n

    @staticmethod #This is for static method and this does not associated with class
    #Now we dont need to pass 'self' parameter in method
    #Now we can call this method using ClassName 
    def add(a,b):
        return a+b

""" result = Calc.add(1,2)
print(result) """

a = Calc(5)
print(a.num)

a.addToNum(6)
print(a.num)

#a.add(1,2)
print(a.add(1,2))