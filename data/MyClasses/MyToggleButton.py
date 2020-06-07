# MyToggleButton Class

# imports
from data.MyClasses.MyLabel import MyLabel
from data.MyClasses.MyButton import MyButton
from data.MyClasses.MyFrame import MyFrame
from data.MyFunctions import GrayScale
from data.MyVariables import MyFonts


class MyToggleButton(object):

    relwidth, relheight, enabled = 0.20, 0.10, False

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely
        self.defaults()

    def defaults(self):
        self.createTitleLabel()
        self.createFrames()

    def createTitleLabel(self):
        self.titleLabel = MyLabel(self.parent, self.text, self.relx, self.rely - 0.05)
        self.titleLabel.configure(font=MyFonts['LargeBold'])

    def createFrames(self):
        self.mainFrame = MyFrame(self.parent, GrayScale(0))
        self.mainFrame.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.frame1 = MyFrame(self.mainFrame, GrayScale(80))
        self.frame2 = MyFrame(self.mainFrame, GrayScale(60))

        self.button1 = MyButton(self.frame1, 'Disabled', self.func1, 0, 0)
        self.button2 = MyButton(self.frame2, 'Enabled', self.func2, 0, 0)
        
        gs20, gs40, gs180 = GrayScale(20), GrayScale(40), GrayScale(180)
        self.button1.configure(bg=gs40, activebackground=gs180, fg=gs20)
        self.button2.configure(bg=gs180, activebackground=gs40, fg=gs20)

        self.button1.place(relwidth=1, relheight=1)
        self.button2.place(relwidth=1, relheight=1)

    def func1(self):
        self.frame2.tkraise()
        self.enabled = True

    def func2(self):
        self.frame1.tkraise()
        self.enabled = False
