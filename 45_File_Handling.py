#For open and read the file
""" f = open('Abhay1.txt','r')
#print(f)
text = f.read()
print(text)
f.close()  """ 

#For open and writer the file or if not exist than create new file
""" f= open('Dubey1.txt','w')
#f= open('Abhay1.txt','w') #This will overwrite the contents
#which is wriiten in previous and add new content #////NOt recommended use append() to add contend
f.write("Hello Dubey, Good Afternoon")
f.close """

#For append thr data in existing file
""" f.open('Abhay1.txt','a')
f.write("Hello Brother, I am Back")
f.close() """

#'with' statement appending
with open('Dubey1.txt','a') as f:
    f.write("\nGood vives")
