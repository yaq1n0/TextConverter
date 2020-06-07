# MyFrame Class

# imports
from tkinter import Frame


class MyFrame(Frame):

    relx, rely, relwidth, relheight = 0, 0, 1, 1

    def __init__(self, parent, bgcolor):
        Frame.__init__(self, parent)

        self.configure_(bgcolor)
        self.place_()

    def configure_(self, bgcolor):
        self.configure(bg=bgcolor)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

