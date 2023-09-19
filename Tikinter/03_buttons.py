from tkinter import *

root = Tk()

def myClick():
    myLable = Label(root, text="")

myButton = Button(root, text=" Click Me! ",padx=10,pady=50)
myButton.pack()

root.mainloop()

