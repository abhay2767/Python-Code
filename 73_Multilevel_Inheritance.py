class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name is: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, bread):
        Animal.__init__(self,name, species="Dog")
        self.bread = bread
    
    def show(self):
        Animal.show(self)
        print(f"Bread is {self.bread}")

class Puppy(Dog):
    def __init__(self,name, color):
        Dog.__init__(self, name, bread="Puppy")
        self.color= color

    def show(self):
        Dog.show(self)
        print(f"Color is: {self.color}")
p = Puppy("Tommy", "Brown")
p.show()