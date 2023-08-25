""" Instance variable vs Class Variable:-
    1-We use "instance Variable" When we have to associate any property with a pariticula
    object.
    2-We use "Class Variable" When we have to create variable for the whole class. which can
    shared by all the instances
"""
class Employee:
    #This is class Variable (This will same for everyone in whole Employee class because thid is associated with class so this is called "Class Variable")
    comp_name = "Apple"
    num_of_emp = 0
    #constructor created
    def __init__(self,name,id):
        self.name = name#Here incoming 'name' will be set to the instance of this class
        self.id = id
        self.bonus = 10000 #this will same for every Employee
        #Because therse are associted with instance
        Employee.num_of_emp += 1

    def showDetaile(self):
        print(f"The Employee of {self.comp_name} with the number of worker {self.num_of_emp} with the id: {self.id} and name: {self.name} have got the bonus of {self.bonus} this year")

emp1 = Employee("Abhay",21689)
#If instance variable is avaiable than will show in emp1 otherwise shown existing given above
emp1.bonus = 15000 
emp1.comp_name = '"Apple India"' 
emp1.showDetaile() 

#Employee.showDetaile(emp1)
#Here Instance variable is not exist so here show the "Class variable which is define in class"
emp2 = Employee("Rajat", 22612)
emp2.comp_name = '"Apple Us"' #here we give the instance variable so this will show
emp2.showDetaile()