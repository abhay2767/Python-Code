#Os module is a built-in module in pyhton
import os

#create 100 folders inside the folder(data)
""" if(not os.path.exists("data")):
    os.mkdir("data") """

""" for i in range(0,100):
    os.mkdir(f"data/Day{i+1}") """

#Rename the folder from day to tutorial
""" for i in range(0,100):
    os.rename(f"data/Day{i+1}", f"data/tutorial{i+1}") """
#os.rename("clutteredPhotos/Return Group 2.pdf","clutteredPhotos/Group Back 2.pdf")

#list all the folder 
""" folders = os.listdir("data")

print(folders) """

#to view the folder(data) inside the folder(tutorial) or inside the folder ie- Abhay.txt
""" for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}")) """

#Currently in which directory you are in
""" print(os.getcwd())
os.chdir("/Users") #change directory
print(os.getcwd()) """

#delete the specific file in folder