name = "Abhay, Rohin";
print(name);
print(len(name)); # Print length of String
print(name[0:3]);  # Print form 0 to 3 "Abh" (0 to n-1) mean 3 will ignored
print(name[:3]); # By deafult start from 0 index
print(name[2:8]); # Print from 2 to 7 "hay, R"

#negative slicing
print(name[0:-3]); # This will print all string except last 3 character
print(name[:len(name)-3]) #Same

print(name[-1:len(name)-3]) #print nothing
print(name[-3:-1]) # total length is 12 here 12-3 = 9 and 12-1 = 11 Mean [-3:-1] = [9:11]

#Quiz
nm = "Harry";
print(nm[-4:-2])