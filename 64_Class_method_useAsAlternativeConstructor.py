#1st way:-
class Employee1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

e1 = Employee1("Abhay",23)
print(e1.name)
print(e1.age)

string = "Dubey-21" #Parse the data from string 
e2 = Employee1(string.split("-")[0],string.split("-")[1]) #This will print like a list ["Abhay",23]
print(e2.name)
print(e2.age)

#2nd way:-
class Employee2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod #Here we use classMethod as Alternative Constructor
    def fromString(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    #Here we parse the String format data

string = "Rohit-24"
e3 = Employee2.fromString(string)
print(e3.name)
print(e3.age)

#Another Example
class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_String(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
""" p = Person.from_String("Abhay,15")
print(p.name,p.age)  """