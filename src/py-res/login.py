from tkinter import *

class MyLogin:
    def __init__(self, myParent):
        self.myContainer1 = Frame(myParent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello, 2222!"
        self.button1["background"] = "green"
        self.button1.pack()