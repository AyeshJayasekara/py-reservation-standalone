from tkinter import *

class Gui:
    def __init__(self, my_parent, parameters):
        self.myContainer1 = Frame(my_parent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello, 2222!"
        self.button1["background"] = "green"
        self.button1.pack()

        my_parent.mainloop()