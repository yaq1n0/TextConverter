# function to generate geometry string from width and height


def makeGeometry(root, width, height):
    x_pos = int((root.winfo_screenwidth() / 2) - (width / 2))
    y_pos = int((root.winfo_screenheight() / 2) - (height / 2))
    geometryString = str(width) + 'x' + str(height) + '+' + str(x_pos) + '+' + str(y_pos)
    return geometryString


if __name__ == '__main__':
    from tkinter import Tk

    test_root = Tk()
    test_geometry = makeGeometry(test_root, 1280, 720)
    test_root.geometry(test_geometry)
    print('function output:', test_geometry)
    test_root.mainloop()
