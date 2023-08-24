class Emp:
    """ name = "Abhay Dubey"
    occ = "Student" """

    def __init__(self,n,o):
        print("Hey I am a Person")
        self.name = n
        self.occ = o


    def info(self):
        print(f"{self.name} is a {self.occ} ")

a = Emp("Abhay","Job")
a.name = "Disha"
a.occ = "Hr"
a.age = 23
print(f"{a.name} is a {a.occ}")
a.info()

b = Emp("Dubey","Self_Employee")
a.info()
b.info()

c= Emp("Rajat", "IAS") #Here 3 argument are pass: "self"- autometicall pass ho rha, "Rajat", "IAS"
