# MyEntry Class

# imports
from tkinter import Entry, RIDGE

from data.MyClasses.MyLabel import MyLabel
from data.MyFunctions import GrayScale
from data.MyVariables import MyFonts


class MyEntry(Entry):
    charwidth, bgcolor, fgcolor = 20, GrayScale(20), GrayScale(220)

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely

        Entry.__init__(self, self.parent)

        self.defaults()

    def defaults(self):
        self.entryConfigure()
        self.entryPlace()
        self.createLabel()

    def entryConfigure(self):
        self.configure(width=self.charwidth, font=MyFonts['Default'],
                       bg=self.bgcolor, fg=self.fgcolor,
                       relief=RIDGE, highlightthickness=2, bd=0)

    def entryPlace(self):
        self.place(relx=self.relx, rely=self.rely)

    def createLabel(self):
        self.label = MyLabel(self.parent, self.text, self.relx, self.rely - 0.050)
        self.label.configure(font=MyFonts['Large'])
