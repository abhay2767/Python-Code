#seek() and tell() function
with open('file.txt','r') as f:
    print(type(f))
    #Move to the 10th bytes in the file
    f.seek(10)

    #Read the next 5 byte
    print(f.tell()) #This will tell you the current position where we are here: 10th
    data = f.read(5)
    print(data)

#truncate() function
with open('sample.txt','w') as f:
    f.write('Hello, Abhay Dubey')
    f.truncate(5)

with open('sample.txt','r') as f:
    print(f.read()) 