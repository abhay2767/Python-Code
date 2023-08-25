class Employee:
    company = "Samsung"
    def show(self):
        print(f"The Name is {self.name} and work in the company is {self.company}")

    @classmethod
    def changeCompany(Aaa, newCompany):#It is adding the company in an 'instance'
        Aaa.company = newCompany
        #cls,self,bike, car,Aaa(kuch bhi likho) ye Samsung hi print krega jab tak ki class ke uper (@classmethod) nhi lagaoge. 
        #(@classmethod) ye lagane ke bad jo change kia h wo print hoga
        #Matlab (@classmethod) ishki help se app "Class variable" change kar skte h
    

    

e1 = Employee()
e1.name = "Abhay"
e1.show()
e1.changeCompany("Apple") 
e1.show()
print(Employee.company)