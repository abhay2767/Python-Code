class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance_type):
        self.dance_type = dance_type

    def show(self):
        print(f"The dance is {self.dance_type}")

class Dancer_Employee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = Dancer_Employee("Kathak", "Shivani")
print(o.name, o.dance)
o.show()
#MRO(method resolution Order):-
print(Dancer_Employee.mro()) #In this order attribute and method search and print