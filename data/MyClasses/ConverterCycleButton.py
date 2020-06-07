# custom class for cycling between different conversions

# imports
from data.MyClasses.MyFrame import MyFrame
from data.MyClasses.MyButton import MyButton
from data.MyFunctions import GrayScale


class ConverterCycleButton(object):
    names_list = ['AltCase', 'RandomCase', 'RegretCase']

    class FullButton(MyButton):
        relx, rely, relwidth, relheight = 0, 0, 1, 1

        def __init__(self, parent, text, command, bgcolor):
            MyButton.__init__(self, parent, text, command, self.relx, self.rely)

            self.configure(bg=bgcolor, activebackground=bgcolor)
            self.place(relwidth=self.relwidth, relheight=self.relheight)

    def __init__(self, parent, relx, rely, relwidth, relheight, parent_self):
        self.parent, self.relx, self.rely, self.relwidth, self.relheight, self.parent_self = parent, relx, rely, relwidth, relheight, parent_self
        self.defaults()

    def defaults(self):
        self.createFrames()
        self.createButtons()

        self.func3()

    def createFrames(self):
        self.mainFrame = MyFrame(self.parent, GrayScale(0))
        self.mainFrame.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.frame1 = MyFrame(self.mainFrame, GrayScale(80))
        self.frame2 = MyFrame(self.mainFrame, GrayScale(60))
        self.frame3 = MyFrame(self.mainFrame, GrayScale(40))

    def createButtons(self):
        self.button1 = self.FullButton(self.frame1, self.names_list[0], self.func1, GrayScale(80))
        self.button2 = self.FullButton(self.frame2, self.names_list[1], self.func2, GrayScale(80))
        self.button3 = self.FullButton(self.frame3, self.names_list[2], self.func3, GrayScale(80))

    def func1(self):
        self.parent_self.titleLabel.configure(text=self.names_list[1])
        self.frame2.tkraise()

        self.parent_self.startCaseToggleButton.titleLabel.destroy()
        self.parent_self.startCaseToggleButton.mainFrame.destroy()

        self.state = 2

    def func2(self):
        self.parent_self.titleLabel.configure(text=self.names_list[2])
        self.frame3.tkraise()
        self.state = 3

    def func3(self):
        self.parent_self.titleLabel.configure(text=self.names_list[0])
        self.frame1.tkraise()
        self.parent_self.createStartCaseToggle()
        self.state = 1
