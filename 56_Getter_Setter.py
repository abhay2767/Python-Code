#In pyhton you can create getters and setters 
#which helps you to use a function's return value as an object's property

class myclass:
    def __init__(self,value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

    @property #This is a getter now
    def Ten_value(self):
        return 10*self._value
    
    @Ten_value.setter #This is a setter now
    def Ten_value(self, new_value):
        self._value = new_value
    
obj = myclass(10)
obj.Ten_value = 67
print(obj.Ten_value)
obj.show()