class Parent_Class:
    def parent_method(self):
        print("This is parent's class method")
    
class Child_Class(Parent_Class):
    def child_method(Self):
        print("This is child's class method")
        #super().parent_method()
    
    def parent_method(self): #method override
        print("This is child's class parent method")
        super().parent_method()
    
child_object = Child_Class()

child_object.child_method()
child_object.parent_method()


class Employee:
    def __init__(self, id ,name):
        self.id = id
        self.name = name

class Programmer(Employee):
    def __init__(self,id, name, lang):
        super().__init__(id, name)
        self.lang = lang

rohan = Programmer(21689, "Abhay Dubey", "Python3")
print(rohan.id,rohan.name,rohan.lang)