# main page class

# imports
from tkinter import END

from data.MyClasses import MyFrame, MyLabel, MyEntry, MyButton, MyToggleButton, ConverterCycleButton
from data.MyFunctions import GrayScale, AltCase, RandomCase, RegretCase
from data.MyVariables import MyFonts
from data.audioLib import sayText


class MainPage(object):
    def __init__(self, root):
        self.root = root

        self.defaults()

    def defaults(self):
        self.createFrame()
        self.createTitle()
        self.createConverterCycleButton()
        self.createConvertButton()
        self.createEntries()
        self.createSpeakButtons()

    def createFrame(self):
        self.mainFrame = MyFrame(self.root, GrayScale(20))

    def createTitle(self):
        self.titleLabel = MyLabel(self.mainFrame, 'Main Page', 0.25, 0.05)
        self.titleLabel.configure(font=MyFonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)

    def createConverterCycleButton(self):
        self.converterCycleButton = ConverterCycleButton(self.mainFrame, 0.70, 0.30, 0.10, 0.05, self)

    def createConvertButton(self):
        self.convertButton = MyButton(self.mainFrame, 'Convert', self.convert, 0.70, 0.15)

    def createEntries(self):
        self.inputEntry = MyEntry(self.mainFrame, 'Input', 0.05, 0.15)
        self.outputEntry = MyEntry(self.mainFrame, 'Output', 0.05, 0.55)

        self.inputEntry.place(relwidth=0.45, relheight=0.30)
        self.outputEntry.place(relwidth=0.45, relheight=0.30)

    def createSpeakButtons(self):
        self.inputSpeakButton = MyButton(self.mainFrame, 'Say Input', self.speakInput, 0.55, 0.15)
        self.outputSpeakButton = MyButton(self.mainFrame, 'Say Output', self.speakOutput, 0.55, 0.55)

    def createStartCaseToggle(self):
        self.startCaseToggleButton = MyToggleButton(self.mainFrame, 'Start Case', 0.70, 0.45)
        self.startCaseToggleButton.mainFrame.place(relwidth=0.10, relheight=0.05)

    def writeto_outputEntry(self, text):
        self.outputEntry.delete(0, END)
        self.outputEntry.insert(0, text)

    def convert(self):
        input_text = self.inputEntry.get()
        output_text = ''

        if input_text != '':
            if self.converterCycleButton.state == 1:
                output_text = AltCase(input_text, self.startCaseToggleButton.enabled)
            elif self.converterCycleButton.state == 2:
                output_text = RandomCase(input_text)
            elif self.converterCycleButton.state == 3:
                output_text = RegretCase(input_text)

            self.writeto_outputEntry(output_text)

    def speakInput(self):
        sayText(self.inputEntry.get())

    def speakOutput(self):
        if self.outputEntry.get() == '':
            if self.inputEntry != '':
                self.convert()

        sayText(self.outputEntry.get())
