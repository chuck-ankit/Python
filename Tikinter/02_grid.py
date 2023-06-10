from tkinter import *
root = Tk()

#Creating a lable widget
mylableL1 = Label(root, text="Hello World!")
mylableL2 = Label(root, text="My name is Ankit kumar")
mylableL3 = Label(root, text="                             ")
#Shoving it onto the screen

mylableL1.grid(row=0, column=0)
mylableL3.grid(row=1, column=1)
mylableL2.grid(row=1, column=5)

root.mainloop()