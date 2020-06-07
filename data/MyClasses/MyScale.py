# MyScale Class

# imports
from tkinter import Scale, Label, StringVar, HORIZONTAL, RIDGE, FLAT

from data.MyFunctions import GrayScale
from data.MyVariables import MyFonts


class MyScale(Scale):
    bgcolor, fgcolor, lowrange, highrange, resolution, s_relwidth, s_relheight = GrayScale(20), GrayScale(
        220), 1.0, 100.0, 0.1, 0.10, 0.05

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely

        Scale.__init__(self, self.parent)

        self.l_val = StringVar()
        self.defaults()

    def defaults(self):
        self.scaleConfigure()
        self.scalePlace()
        self.labelCreate()

    def scaleConfigure(self):
        self.configure(command=self.update,
                       from_=self.lowrange, to=self.highrange,
                       orient=HORIZONTAL, showvalue=0, resolution=self.resolution,
                       bg=self.bgcolor, fg=self.fgcolor,
                       relief=RIDGE, highlightthickness=0, bd=0)

    def scalePlace(self):
        self.place(relx=self.relx, rely=(self.rely + 0.01), relwidth=self.s_relwidth, relheight=self.s_relheight)

    def createLabel(self):
        self.label = Label(self.parent)

        self.labelConfigure()
        self.labelPlace()

    def labelConfigure(self):
        self.label.configure(textvariable=self.l_val,
                             font=MyFonts['Large'],
                             bg=self.bgcolor, fg=self.fgcolor,
                             relief=FLAT,
                             padx=2, pady=2)

    def labelPlace(self):
        self.label.place(relx=self.relx, rely=self.rely - 0.050)

    def update(self, *args):
        self.l_val.set(self.text + ' = ' + str(Scale.get(self)))
