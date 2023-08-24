class Details:
    name = "Abhay"
    age = 23
    Occupation = "Job"
    Address = "Delhi"
    def info(self):
        print(f"{self.name} age is {self.age}")
        #self: meaning- {Wo Object jiske liye ye Method call kiya ja rha h}

a = Details()
a.name = "Rohit"
a.age = 21
a.Occupation = "Self_Employeee"
a.Address = "Utter Pradesh"

b = Details()
c = Details()

print(a.name," is a ", a.Occupation," and lives in ",a.Address," and his age is ",a.age)
print(f"{a.name}  is a {a.Occupation}")
a.info()