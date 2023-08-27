# __len__ method:-
from Emp_67 import Employee
""" class Employee:
    name = "Abhay"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i """

a = Employee("Abhay_Dubey")
print(str(a))
print(repr(a))
a( )
print("Length of name is: ",len(a))