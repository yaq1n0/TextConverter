# random capitals

# imports
from data.MyFunctions.textConversion.dependencies import randBool, letters


def RandomCase(input_text):
    if type(input_text) != str:
        print('[RandomCase] Input not a string')
        return None

    else:
        input_text = input_text.lower()
        return_string = ''

        for letter in input_text:
            if letter in letters:
                if randBool():
                    return_string += letter.upper()
                else:
                    return_string += letter.lower()
            else:
                return_string += letter

        return return_string


if __name__ == '__main__':
    test_string = 'Hello World'
    print('[test]:', RandomCase(test_string))
