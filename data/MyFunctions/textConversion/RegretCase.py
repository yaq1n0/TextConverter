# regret case

# imports
from data.MyFunctions.textConversion.dependencies import pickRandomList, replaceWord, short_cringe, long_cringe


def RegretCase(text):
    if type(text) != str:
        print('[RegretCase] Input not a string')
        return None

    else:
        text = text.lower()
        return_string = ''

        pl = ''

        for letter in text:
            if letter == 'r' and pl != 'l':
                return_string += 'w'

            elif letter == 'l' and pl != 'r':
                return_string += 'w'

            elif letter == ' ' and pl != '.':
                return_string += (' ' + pickRandomList(short_cringe) + ' ')

            elif letter == '.':
                return_string += (' ' + pickRandomList(long_cringe) + ' ')

            else:
                return_string += letter

            pl = letter

        return_string = replaceWord(return_string)

        return return_string


if __name__ == '__main__':
    test_string = 'Hello World. yes '
    print('[test]:', RegretCase(test_string))
