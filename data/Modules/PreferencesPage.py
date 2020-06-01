# preferences page class

# imports
from os import execv
from sys import executable, argv
from tkinter import END
from tkinter.messagebox import showinfo, showwarning

from data.MyClasses import MyFrame, MyLabel, MyToggleButton, MyImageButton, MyEntry
from data.MyFunctions import GrayScale, createTkImage, writePreferences
from data.MyVariables import MyFonts

from data.MyVariables.preferences import width as config_width
from data.MyVariables.preferences import height as config_height
from data.MyVariables.preferences import font as config_font
from data.MyVariables.preferences import font_size as config_font_size
from data.MyVariables.preferences import tooltips as config_tooltips
from data.MyVariables.preferences import dev


# restart and quit functions
def programRestart():
    if dev:
        print('[program] restart')
    # code from 'https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/'
    execv(executable, ['python'] + argv)


def programQuit():
    if dev:
        print('[program] quit')
    exit()


class PreferencesPage(object):
    def __init__(self, root):
        self.root = root

        self.defaults()

    def defaults(self):
        self.createFrame()
        self.createTitle()
        self.createWidthEntry()
        self.createHeightEntry()
        self.createFontEntry()
        self.createFontSizeEntry()
        self.createToolTipToggle()
        self.createDevToggle()
        self.createResetButton()
        self.createSaveButton()

        self.setAll()

    def createFrame(self):
        self.mainFrame = MyFrame(self.root, GrayScale(20))

    def createTitle(self):
        self.title_label = MyLabel(self.mainFrame, 'Modify Program Settings', 0.05, 0.05)
        self.title_label.configure(font=MyFonts['ExtraLargeBold'])
        self.title_label.place(relwidth=0.9)

    def createWidthEntry(self):
        self.width_entry = MyEntry(self.mainFrame, 'Window Width (pixels)', 0.25, 0.20)
        self.width_entry.label.place(relwidth=0.90, relx=0.05)
        self.width_entry.place(relwidth=0.50)

    def createHeightEntry(self):
        self.height_entry = MyEntry(self.mainFrame, 'Window Height (pixels)', 0.25, 0.325)
        self.height_entry.label.place(relwidth=0.90, relx=0.05)
        self.height_entry.place(relwidth=0.50)

    def createFontEntry(self):
        self.font_entry = MyEntry(self.mainFrame, 'Font Name', 0.25, 0.450)
        self.font_entry.label.place(relwidth=0.90, relx=0.05)
        self.font_entry.place(relwidth=0.50)

    def createFontSizeEntry(self):
        self.font_size_entry = MyEntry(self.mainFrame, 'Font Size (points)', 0.25, 0.575)
        self.font_size_entry.label.place(relwidth=0.90, relx=0.05)
        self.font_size_entry.place(relwidth=0.50)

    def createToolTipToggle(self):
        self.tooltips_button = MyToggleButton(self.mainFrame, 'Tooltips', 0.20, 0.70)

    def createDevToggle(self):
        self.dev_button = MyToggleButton(self.mainFrame, 'Developer', 0.60, 0.70)

    def createResetButton(self):
        self.reset_button = MyImageButton(self.mainFrame, GrayScale(20), createTkImage('data/images/reset.png', 48, 48),
                                          self.funcReset, 0.30, 0.85)
        self.reset_button.place(relwidth=0.14, relheight=0.07)

    def createSaveButton(self):
        self.save_button = MyImageButton(self.mainFrame, GrayScale(20), createTkImage('data/images/save.png', 48, 48),
                                         self.funcSave, 0.56, 0.85)
        self.save_button.place(relwidth=0.14, relheight=0.07)

    def clearALL(self):
        # clear all entries in GUI
        self.width_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.font_entry.delete(0, END)
        self.font_size_entry.delete(0, END)

    def setAll(self):
        # set all entries in GUI from imported vars from userconfig.py
        self.clearALL()

        self.width_entry.insert(0, str(config_width))
        self.height_entry.insert(0, str(config_height))
        self.font_entry.insert(0, str(config_font))
        self.font_size_entry.insert(0, str(config_font_size))

        if config_tooltips:
            self.tooltips_button.func1()
        else:
            self.tooltips_button.func2()

        if dev:
            self.dev_button.func1()
        else:
            self.dev_button.func2()

    def checkAll(self):
        # checking that values are reasonable
        # currently only checks that resolution is 16 by 9 and is a common resolution
        input_width = self.width_entry.get()
        input_height = self.height_entry.get()

        width_list = ['1280', '1920', '2560', '3840']
        height_list = ['720', '1080', '1440', '2160']

        if input_width not in width_list \
                or input_height not in height_list \
                or float(input_width) / float(input_height) != 16.0 / 9:
            showwarning('Resolution Warning!', 'You have selected a non standard resolution\n'
                                               'This may cause visual errors\n')
            return True

        else:
            return True

    def funcReset(self):
        # reset to defaults
        self.clearALL()

        self.width_entry.insert(0, '1280')
        self.height_entry.insert(0, '720')
        self.font_entry.insert(0, 'Helvetica')
        self.font_size_entry.insert(0, '12')

        setattr(self.tooltips_button, 'enabled', True)
        self.tooltips_button.f2.tkraise()

        setattr(self.dev_button, 'enabled', True)
        self.dev_button.f2.tkraise()

    def funcSave(self):
        # save and write to config
        if self.checkAll():
            writePreferences(self.width_entry.get(),
                             self.height_entry.get(),
                             self.font_entry.get(),
                             self.font_size_entry.get(),
                             getattr(self.tooltips_button, 'enabled'),
                             getattr(self.dev_button, 'enabled')
                             )

        showinfo('Settings Saved', 'Settings Saved, click OK to restart')

        programRestart()
