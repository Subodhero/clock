from tkinter import *
from time import *

def update():
    time_stirng=strftime("%I:%M:%S %p")
    time_label.config(text=time_stirng)

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window=Tk()

time_label = Label(window, font=("ARIAL", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("italic", 25),fg="black")
day_label.pack()

date_label = Label(window, font=("italic", 30),fg="black")
date_label.pack()

name_label = Label(window, text="made by Subodh", font=("italic", 10),fg="black")
name_label.pack()

window.title("clock made by subodh")
icon=PhotoImage(file="E:\my progects\python\Project\logo.png")
window.iconphoto(True,icon)

update()

window.mainloop()