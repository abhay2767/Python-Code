#In simple word 'Object Introspection' means you want to know, what is present in an Object.
#dir():-
x = [1,2,3]
#print(dir(x)) #This will print all methods and attributes that we can use and apply on list.
"""
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 """
print(x.__eq__)
print(x.__dir__)
print(x.__str__)

# __dict__:- it is a attribute
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Abhay",23)
print(p)
print(p.__dict__) #This will print in format of dictinary object

#help():
print(help(Person))