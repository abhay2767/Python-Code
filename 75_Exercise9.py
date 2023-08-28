""" Write a program to pronounce list of names using win32 API.
    If you given a list l as follow:-
    l = ["Abhay","Rohit","Rajat","Sachin","Anshu"]
    Your Program should pronounce the names
 """
#for Mac
""" from os import system
names = ["Abhay","Rohit","Rajat","Sachin","Anshu"]
for name in names:
    system(f"say shoutout to {name}") """

#for window
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
""" text = "Python text-to-speech test. using win32com.client"
speak.Speak(text) """ #for single text
names = ["Abhay","Rohit","Rajat","Sachin","Anshu"]
for name in names:
    speak.Speak(f"say shoutout to {name}")