# MyImageButton Class

# imports
from tkinter import Button, RIDGE


class MyImageButton(Button):

    # optimized for 16:9 windows
    relwidth, relheight = 0.05 / (16.0 / 9.0), 0.05

    def __init__(self, parent, bgcolor, img, command, relx, rely):
        self.bgcolor, self.abgcolor, self.img, self.command, self.relx, self.rely = bgcolor, bgcolor, img, command, relx, rely

        Button.__init__(self, parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(command=self.command,
                       bg=self.bgcolor, activebackground=self.abgcolor,
                       relief=RIDGE, highlightthickness=0, bd=0,
                       image=self.img)
        self.image = self.img

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
