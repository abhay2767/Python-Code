a = "Abhay ji Abhay"
print(a)
print("Length is ",+len(a))
 
#Strings are immutable means cant not change but can create a copy of string
#Strings methods can not change the acutual string but can create a new string
# and perfrom operation on that string
print(a.upper())
print(a.lower())

#strip unneccesary marks
Name = "Abhay Dubey#@!"
print(Name)
print(Name.rstrip("@,!,#"))

#Replace
print(a) 
print(a.replace("Abhay", "Dubey")) # replace all occurences

#Split (This will convert string in list)
print(a.split(" "))

#Capitalized (This is not java script)
BlogHeading = "introduCtion To pyTHon";
print(BlogHeading)
print(BlogHeading.capitalize())

#center
str = "Wellcome the the console";
print(str)
print("Lenght before method is ", +len(str))
print(str.center(50)) # This will gives 50 time space
print("Length after method is ",len(str.center(50)))

#count
print(a.count("Abhay")) #how much time Abhay is written in 'a' string

#endswith
str1 = "Wellcome the java script @!!!!!"
print(str1.endswith("@"))
print(str1.endswith("!"))

#startswith
str1 = "@Pyhton is interpreted Language"
print(str1.startswith("@"))

#we can even also check for a value in-between the string by providing start and end index position
print(str1.endswith("come t", 4, 10))
print(str1.endswith("java", 4, 10))

#find (search for first occurence in string and return its index or if not avaible return -1)
b= "He is a y good boy"
print(b.find("y"))
print(b.find("z"))

#index
print(b.index("He"))
#print(b.index("Hee"))

#isalnum (return true only if the entire string only consist of A-Z, a-z, 0-9)
#if any other character or punctuations are present , then it return false
str2 = "WellcomeToTheWorldOfProgramming263";
print(str2.isalnum())

#isalpha (return true only if the entire string only consist of A-Z, a-z)
#if any other character or punctuations or number(0-9) are present , then it return false
str3 = "WellcomeToTheWorldOfProgramming5";
print(str3.isalpha())

#islower (return true if all the characters in string are in lowercase)
str4 = "dfjvisdjskhsf"
print(str4.islower())

#islower (return true if all the characters in string are in uppercase)
str4 = "adfjvisdjskhsf"
print(str4.isupper())

#isprintable (return true if all value within the given string are printable)
str5  = "Hello Abhay Dubey "
print(str5.isprintable())

str6  = "Hello Abhay Dubey \n"
print(str6.isprintable())

#isspace (return true if there are any white space in string)
str7 = "      "
print(str7.isspace())

str8 = "    "#using Tab
print(str8.isspace)

#istitle (return true if the first letter of each word of the string is capatialized)
str8 = "World Health organisation "
print(str8.istitle)

#swapcase (convert lower to upper and upper to lower)
str9 = "This is a Labtop"
print(str9.swapcase())

#title (all first leter of word will be capital)
str10 = "his name is Abhay Dubey"
print(str10.title())
