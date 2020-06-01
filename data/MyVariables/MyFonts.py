# dictionary of App fonts

# imports
from data.MyVariables.preferences import font, font_size

MyFonts = {
    'Default': (font, font_size),
    'DefaultBold': (font, font_size, 'bold'),
    'Small': (font, int(round(font_size * 0.75, 0))),
    'SmallBold': (font, int(round(font_size * 0.75, 0)), 'bold'),
    'Large': (font, int(round(font_size * 1.25, 0))),
    'LargeBold': (font, int(round(font_size * 1.25, 0)), 'bold'),
    'ExtraLarge': (font, int(round(font_size * 1.50, 0))),
    'ExtraLargeBold': (font, int(round(font_size * 1.50, 0)), 'bold')
}

if __name__ == '__main__':
    for elem in MyFonts:
        print(elem, ':', MyFonts[elem])
