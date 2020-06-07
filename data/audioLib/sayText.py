# function to say input text

# imports
from random import randint
from json import load, dumps
from gtts import gTTS
from playsound import playsound
from os import listdir, path, remove

from time import time

language = 'fr'
cachedAudio = {}
minDigits = 1

if __name__ == '__main__':
    audio_path = 'audioCache/'
    json_path = 'cachedAudio.json'

else:
    audio_path = 'data/audioLib/audioCache/'
    json_path = 'data/audioLib/cachedAudio.json'


def readJSON():
    # read JSON from json_path, write to cachedAudio
    global cachedAudio

    with open(json_path, 'r') as json_file:
        cachedAudio = load(json_file)

    return None


def writeJSON():
    # read from cachedAudio, write to JSON at json_path
    global cachedAudio

    with open(json_path, 'w') as json_file:
        json_file.write(dumps(cachedAudio))

    return None


def preprocessText(text):
    # return 'Field Empty' if input is '', strip() text regardless
    if text == '':
        text = 'Field Empty'

    text = text.strip()

    return text


def generateKey():
    # return random key string not already in cachedAudio
    global cachedAudio, minDigits

    def generateRandomKey():
        # return random key string
        global minDigits

        def maxRange():
            # return MaxRange with minDigits
            global minDigits

            MaxRange = ''
            for i in range(minDigits):
                MaxRange += '9'

            return int(MaxRange)

        while len(cachedAudio) > maxRange():
            minDigits += 1

        key = str(randint(0, maxRange()))
        while len(key) < minDigits:
            key = '0' + key

        return key

    key = generateRandomKey()
    while key in cachedAudio:
        key = generateRandomKey()

    return key


def KeyToFilePath(key):
    # return corresponding file path (string) of key (string)
    file_path = audio_path + key + '.mp3'
    return file_path


def entryInDict(entry):
    # return array with boolean as to whether input_entry is in input_dict,
    # if yes, return key of input_entry, else return placeholder key of '0000'

    for key in cachedAudio:
        if entry == cachedAudio[key]:
            return [True, key]

    return [False, '0000']


def createAudioCache(text):
    # generate unique key, and corresponding path
    key = generateKey()
    audioObjPath = KeyToFilePath(key)

    # create audio object
    audioObj = gTTS(text=text, lang=language)

    # save audio object to path
    audioObj.save(audioObjPath)

    # save to runtime dictionary, save to JSON
    cachedAudio[key] = text
    writeJSON()


def sayText(text):
    global cachedAudio

    # check for empty input, strip()
    text = preprocessText(text)

    # load JSON
    readJSON()

    # check in cachedAudio
    inAudioCache = entryInDict(text)

    if not inAudioCache[0]:
        # create AudioCache if not present
        createAudioCache(text)
        inAudioCache = entryInDict(text)

    # play audio
    playsound(KeyToFilePath(inAudioCache[1]))


def clearAudioCache():
    global cachedAudio
    lsAudioCache = [_file for _file in listdir(audio_path)]

    for _file in lsAudioCache:
        remove(path.join(audio_path, _file))

    cachedAudio = {}
    writeJSON()


if __name__ == '__main__':
    from tkinter import Tk, Entry, Button
    from data.MyFunctions import makeGeometry

    test_root = Tk()
    test_root.geometry(makeGeometry(test_root, 200, 100))
    test_entry = Entry(test_root)
    test_entry.pack()


    def sayTextTest(event):
        sayText(test_entry.get())

    def exitBind(event):
        exit()

    def overflowTest():
        clearAudioCache()

        for n in range(1000):
            createAudioCache(str(n))

    test_root.bind('<Return>', sayTextTest)
    test_root.bind('<Escape>', exitBind)

    Button(test_root, text='ClearAudioCache', command=clearAudioCache).pack()
    Button(test_root, text='OverflowTest', command=overflowTest).pack()

    test_entry.focus()

    test_root.mainloop()



