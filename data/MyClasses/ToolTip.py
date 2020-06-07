# ToolTip class

# imports
from tkinter import Toplevel, Label, LEFT, SOLID

from data.MyFunctions import GrayScale
from data.MyVariables import MyFonts


# code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python'
class ToolTip(object):
    def __init__(self, widget):
        self.widget, self.tipwindow, self.id, self.x, self.y = widget, None, None, 0, 0

    def showtip(self, text):
        # showtip method for ToolTip class
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 30
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = Label(tw, text=self.text)
        label.configure(justify=LEFT,
                        relief=SOLID, bd=1,
                        bg=GrayScale(60), fg=GrayScale(220),
                        font=MyFonts['Default'])
        label.pack(ipadx=1)

    def hidetip(self):
        # hidetip method for ToolTip class
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

