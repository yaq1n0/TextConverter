# function to create a Tk compatible image

# imports
from tkinter import Tk, Label
from PIL import Image, ImageTk

from data.MyFunctions.makeGeometry import makeGeometry


def createTkImage(path, x_size, y_size):
    img_open = Image.open(path)
    img_resized = img_open.resize((x_size, y_size), Image.ANTIALIAS)
    img_Tk = ImageTk.PhotoImage(img_resized)
    return img_Tk


if __name__ == '__main__':
    test_root = Tk()
    test_root.geometry(makeGeometry(test_root, 500, 500))
    _img = createTkImage('../images/test.png', 500, 500)
    picture_label = Label(test_root, image=_img)
    picture_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    test_root.mainloop()
