""" Write a program to clear the clutter inside a folder on your computer.
    you should use os Module to rename all the png images from 1.png all the way till n.png
    where n is the number of png files that folder.
    Do the same for other file formats
 """

#Operation system module(Os module):
import os

#os.rename("clutteredPhotos/Return Group 2.pdf","clutteredPhotos/Group Back 2.pdf")
""" folder = set(os.listdir("clutteredPhotos"))
print(folder) """
files = os.listdir("clutteredPhotos")
i = 1
for file in files:
    if(file.endswith(".png")):
        print(file)
        os.rename(f"clutteredPhotos/{file}", f"clutteredPhotos/{i}.png")
        i = i+1