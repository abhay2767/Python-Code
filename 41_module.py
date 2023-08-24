import lxml as pd
import pandas
import math
from math import sqrt # for importing specific function from module not whole module
from math import pi, floor #for importing multiple function from module not whole module
from math import * #for importing everythingh from math module ////Not recommended

import math as m #now you can use m instead of math
from math import floor as f
data = m.sqrt(10)
data1 = f(12.555)
print(data, data1)

print(pd.__version__) #for version


#pandas.read_csv()

result = floor(4.2359)
result1 = sqrt(9)
print(result)
print(result1)


print(dir(math)) #dir function will help you to view all variable and function of module
print(dir(pd)) #Above lxml as pd declared so we use pd instead of lxml
print(type(math.pi)) #this is a class float

#import function of another pyhton program file
# (Abhay is a file name and Dubey is a variable and wishes is a function, all are inside Abhay)
from Abhay import wishes, Dubey
#or
from Abhay import*
#or
from Abhay import Dubey as d

wishes()
print(Dubey)
print(d)