# functions related to writing to preferences.py


def writePreferences(new_width, new_height, new_font, new_font_size, new_tooltips, new_dev):
    # converting all inputs to string
    array = [new_width, new_height, new_font, new_font_size, new_tooltips, new_dev]
    array = list(map(str, array))

    if __name__ == '__main__':
        _path = '../MyVariables/preferences.py'
    else:
        _path = 'data/MyVariables/preferences.py'

    preferences = open(_path, 'w')
    preferences.writelines([
        '\n',
        '# preferences \n',
        'width = ' + array[0] + '\n',
        'height = ' + array[1] + '\n',
        'font = "' + array[2] + '"\n',
        'font_size = ' + array[3] + '\n',
        'tooltips = ' + array[4] + '\n',
        'dev = ' + array[5] + '\n',
    ])
    preferences.close()

    return None


def writeDefaultPreferences():
    writePreferences(1280, 720, 'Helvetica', 12, True, True)

    return None


if __name__ == '__main__':
    writeDefaultPreferences()
    print(open('../MyVariables/preferences.py', 'r').read())
