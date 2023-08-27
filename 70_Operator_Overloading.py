class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return vector(self.i+x.i, self.j+x.j, self.k+x.k)
    
v1 = vector(3,5,6)
print("vector v1:- :",v1)
v2 = vector(3,5,6)
print("vector v2:- :",v1)
print("              ______________")
print("Addition is: ",v1+v2)
print("              ______________")
print("data type is: ",type(v1+v2))