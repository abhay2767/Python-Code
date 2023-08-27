class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self): #__str__ method:-
        return f"Employee is {self.name} str" 
    
    def __repr__(self): #repr method:-
        return f"Employee is {self.name} repr"
    
    def __call__(self):
        print("Hey i am call method")