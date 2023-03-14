from tkinter import *
from tkinter import ttk

import pyttsx3
engine = pyttsx3.init()

win = Tk()

win.geometry("700x250")

def get_data():
    engine.say(entry.get("1.0",END))
    engine.runAndWait()

def clear():
    entry.delete("1.0",END)

entry = Text(win, width= 24, height= 5, font=('Helvetica 25'))
entry.place(relx= .35, rely= .5, anchor= CENTER)

label= Label(win, text="", font=('Helvetica 13'))
label.pack()

ttk.Button(win, text= "Click to Speak", command= get_data).place(relx= .85, rely= .4, anchor= CENTER)
ttk.Button(win, text= "Clear", command= clear).place(relx= .85, rely= .6, anchor= CENTER)

win.mainloop()