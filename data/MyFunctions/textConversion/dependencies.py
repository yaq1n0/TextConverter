# dependencies for other textConversion functions

# imports
from random import randint

# constant
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# modify to add
replace_dict = {
    'rawr ': 'rawr x3',
    'neck ': 'necky wecky ~murr~ ',
    'likes ': 'likies (; ',
    'yes ': 'nya~ ',
    'mhm ': 'mhm~ '
}

short_cringe = ['xD', 'x3', '~', '!!', ';)', ':3']

long_cringe = ['uwu.', 'owo.', 'UwU.', 'OwO.', 'UmU.', 'OmO.',
               'uwu!', 'owo!', 'UwU!', 'OwO!', 'UmU!', 'OmO!']


def randBool():
    # return True or False randomly at roughly 50/50 chances
    var = randint(0, 1)
    if var == 1:
        return True
    else:
        return False


def pickRandomList(list):
    # pick a random element from a list
    return list[randint(0, len(list) - 1)]


def replaceWord(text):
    # replace word in text using replace_dict
    for elem in replace_dict:
        text = text.replace(elem, replace_dict[elem])
    return text


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

    def testALL():
        printValues()
        print('----------------')
        randBoolTest()
        print('----------------')
        pickRandomListTest()
        print('----------------')
        replaceWordTest()
        print('----------------')
        print('ALL tests complete')

    test_choice = input('pick test (printValues, randBool, pickRandomList, replaceWord, ALL): ')
    choice_list = ['printValues', 'randBool', 'pickRandomList', 'replaceWord', 'ALL']

    while test_choice not in choice_list:
        print('invalid input!')
        test_choice = input('pick test (printValues, randBool, pickRandomList, replaceWord, ALL): ')

    if test_choice == 'printValues':
        printValues()

    elif test_choice == 'randBool':
        randBoolTest()

    elif test_choice == 'pickRandomList':
        pickRandomListTest()

    elif test_choice == 'replaceWord':
        replaceWordTest()

    elif test_choice == 'ALL':
        testALL()


