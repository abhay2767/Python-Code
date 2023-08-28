import shutil

#shutil.copy("Abhay.jpg", "clutteredPhotos/Abhay.jpg")
""" This will copy file from location to another """

#shutil.copy2("Dubey.jpg","clutteredPhotos/Dubey.jpg")
""" Same as above but This will copy file and also exact copy like with date time from location to another """

#shutil.copytree("data", "clutteredPhotos/data1")
""" This will copy whole folder to another location """

#shutil.move("clutteredPhotos/data1", ".data2")
""" This will move the file to another destination """

#shutil.rmtree(".data2")
""" This will permanatly delete the file """