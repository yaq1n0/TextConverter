# regret case

# imports
from data.MyFunctions.textConversion.dependencies import replaceWord, replaceLetter


def RegretCase(text):
    if type(text) != str:
        print('[RegretCase] Input not a string')
        return None

    else:
        text = text.lower()
        text = replaceWord(text)
        text = replaceLetter(text)
        return text


if __name__ == '__main__':
    test_string = 'Hello World. '
    print('[test]:', RegretCase(test_string))
