#Pyhton m Access modifire nhi hote
#Pyhton m Access modifire nhi hote
#Pyhton m Access modifire nhi hote
""" class Vehical:
    def __init__(self,name,model):
        self.name = name
        self.model = model
    print("The data is here")
    def show(self):
        print(f"{self.model} Model car name is {self.name} ")

car = Vehical("Alto", 2008)
car.show() """

#Public Specifier/Modifier
class Employee:
    def __init__(self):
        self.name = "Abhay"

a = Employee()
print(a.name)

#Private Specifier/modifier:-  (__)
class Student:
    def __init__(self,name):
        self.__name = "Dubey" #An indication of private variable

    def __result(self): #An indication of private function
        print(f"This is name of the student is: {self.__name}")

class subject(Student):
    pass

a = Student("Abhay")

#print(a.name)  #Can not access Directlt
#Can not acces varibe because above we declared as Private(__) before initialize (self.__name)

print(a._Student__name) #Access private variable
a._Student__result() #Access private function

#But there is a way to access that varibale like this (_ClassName__variableName)
#But there is a way to access that function like this (_functionName)

#This is (Name Mangling)
print(a.__dir__()) #This we give you a list that which attribute an perform on object a

#Protected specifier/modifier
class Animal:
    def __init__(self):
        self.name = "Cow"

    def _func(self): #Protected function
        return "Elephant"
    
class varity(Animal):
    pass

obj = Animal()
obj1 = varity()

#USing Object of Base class (Animal)
print(obj._func()) #Access protected method using (_) before functionName

#Using Object of Derived Class(varity)
print(obj1._func()) #Access protected method using (_) before functionName
