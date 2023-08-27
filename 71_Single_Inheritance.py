class Animal:
    def __init__(self, name, spices):
        self.name = name
        self.spices = spices
    
    def make_sound(self):
        print("The Sound make by animal")

class Dog(Animal):
    def __init__(self, name, bread):
        Animal.__init__(self, name, spices="Dog")
        self.bread = bread

    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "dog")
a.make_sound()