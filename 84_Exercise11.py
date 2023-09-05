""" Drink Water Reminder:-
        Write a pyhton program whick reminds you of drinking water every hour or two hour.
        Your program can either beep or send desktop notification for a specific opeartion system
 """

#pip install win10toast
from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    "Notification",
    "Notification body",
    duration = 20,
    icon_path = "icon.ico",
    threaded = True,
)