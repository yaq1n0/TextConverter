# alternating capitals

# imports
from data.MyFunctions.textConversion.dependencies import letters


def AltCase(input_text, start_caps):

    if type(input_text) != str or type(start_caps) != bool:
        if type(start_caps) != bool:
            print('[AltCase] start_caps value not boolean')
        else:
            print('[AltCase] Input not a string')
        return None

    else:
        input_text = input_text.lower()
        return_string = ''

        # if start_caps then first letter capital, else first letter lowercase
        if type(start_caps) == bool:
            if start_caps:
                i = True
            else:
                i = False
        else:
            print('[AltCase], invalid start_caps value, use boolean')
            return None

        for letter in input_text:
            if letter in letters:
                if i:
                    return_string += letter.upper()
                    i = False
                else:
                    return_string += letter.lower()
                    i = True
            else:
                return_string += letter

        return return_string


if __name__ == '__main__':
    test_string = 'Hello World'
    print('[test] start_caps True:', AltCase(test_string, True))
    print('[test] start_caps False:', AltCase(test_string, False))
