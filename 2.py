#Import the necessary libraries
from tkinter import *
from datetime import date
#create window
root = Tk()
root.title('getting started with widgets!' )
root.geometry('400x300')

#add widgets
#add title
lbl = Label(text="hey whatsup!", fg="white", bg="072F5F", height=1, width=400)
#add lbl to get a name
#use entry widgets
namelbl = Label(text="full_name", bg="3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global Message
    Message = "hey welcome to the app!"
