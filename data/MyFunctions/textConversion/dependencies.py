# dependencies for other textConversion functions

# imports
from random import randint

# do NOT modify
letters, vowels, consonants = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], \
                              ['a', 'e', 'i', 'o', 'u'], \
                              ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                               'x', 'y', 'z']

# can modify
replace_dict = {
    'rawr ': 'rawr x3',
    'neck ': 'necky wecky ~murr~ ',
    'likes ': 'likies (; ',
    'yes ': 'nya~ ',
    'mhm ': 'mhm~ ',
    'no': 'nyo'
}

short_cringe = ['xD', 'x3', '~', '!!', ';)', ':3']

long_cringe = ['uwu.', 'owo.', 'UwU.', 'OwO.', 'UmU.', 'OmO.',
               'uwu!', 'owo!', 'UwU!', 'OwO!', 'UmU!', 'OmO!']


def randBool():
    # return random boolean value
    var = randint(0, 1)
    if var == 1:
        return True
    else:
        return False


def pickRandomList(input_list):
    # return a random element from a list
    return input_list[randint(0, len(input_list) - 1)]


def replaceWord(text):
    # replace words in text using replace_dict then return
    for elem in replace_dict:
        text = text.replace(elem, replace_dict[elem])
    return text


def replaceLetter(text):
    # replace letters conditionally
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

    return return_string


if __name__ == '__main__':
    def printValues():
        print('letters:', letters)
        print('vowels:', vowels)
        print('consonants:', consonants)
        print('replace_dict:', replace_dict)
        print('short_cringe:', short_cringe)
        print('long_cringe:', long_cringe)


    def randBoolTest():
        print('randBool test')

        # pick a random boolean value 1,000,000 times and check even distribution
        n, m = 0, 0

        for loop in range(1000000):
            i = randBool()
            if i:
                n += 1
            else:
                m += 1

        print('relative distribution for random boolean function: ' + str(n) + ' True and ' + str(m) + ' False')

        print('randBool test complete!')


    def pickRandomListTest():
        print('pickRandomList test')

        test_list = ['a', 'b', 'c', 'd']
        print('test list:', test_list)
        print('random from test list:', pickRandomList(test_list))

        print('pickRandomList test done!')


    def replaceWordTest():
        print('replaceWord test')

        test_word = 'rawr '
        print('test word:', test_word)
        print('test replace:', replaceWord(test_word))

        print('replaceWord test done!')

    def replaceLetterTest():
        print('replaceLetter test')

        test_word = 'Hello World'
        print('test word:', test_word)
        print('test replace:', replaceLetter(test_word))

        print('replaceWord test done!')


    def testALL():
        printValues()
        print('----------------')
        randBoolTest()
        print('----------------')
        pickRandomListTest()
        print('----------------')
        replaceWordTest()
        print('----------------')
        replaceLetterTest()
        print('----------------')
        print('ALL tests complete')


    choice_list = ['printValues', 'randBool', 'pickRandomList', 'replaceWord', 'replaceLetter', 'ALL']

    last_index = len(choice_list) - 1
    prompt_text = 'pick test ('

    for elem in choice_list:
        prompt_text += elem
        if choice_list.index(elem) != last_index:
            prompt_text += ', '

    prompt_text += ') or "END" to exit: '

    exitBool = False

    while not exitBool:
        test_choice = input(prompt_text)

        choice_list.append('END')
        while test_choice not in choice_list:
            print('invalid input!')
            test_choice = input(prompt_text)

        if test_choice == 'printValues':
            printValues()

        elif test_choice == 'randBool':
            randBoolTest()

        elif test_choice == 'pickRandomList':
            pickRandomListTest()

        elif test_choice == 'replaceWord':
            replaceWordTest()

        elif test_choice == 'replaceLetter':
            replaceLetterTest()

        elif test_choice == 'ALL':
            testALL()

        elif test_choice == 'END':
            exitBool = True
