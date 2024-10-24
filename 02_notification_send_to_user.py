# from terminal we use this two different commands

# 1) zenity --info --text="This is a notification message"
# 2) notify-send "Title" "This is the notification message"


# This for like an alert in js
# import subprocess

# def send_notification(title, message):
#     subprocess.run(['notify-send', title, message])

# # Example usage
# send_notification("Good Morning ", "Time to drink water")


# Another like promt
import os
import time

# command = '''zenity --entry --text="Please enter your name:"'''
# os.system(command)

command = '''zenity --file-selection --title="Select a File"'''
name = os.popen(command).read().strip()

with open(name, "rb") as source:
    with open("pdf.pdf", "wb") as file:  # here we give .py extention then we can copy python file
        file.write(source.read())
