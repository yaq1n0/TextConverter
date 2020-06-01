# template case

# imports
from data.MyFunctions.textConversion.dependencies import *


def TemplateCase(text):
    if type(text) != str:
        print('[TemplateCase] Input not a string')
        return None

    else:
        text = text.lower()
        return_string = ''

        for letter in text:
            if letter in letters:
                return_string += letter
            else:
                return_string += letter

        return return_string


if __name__ == '__main__':
    test_string = 'Hello World'
    print('[test]:', TemplateCase(test_string))
