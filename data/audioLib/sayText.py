# function to say input text

# imports
from random import randint
from json import load, dumps
from gtts import gTTS
from playsound import playsound
from os import listdir, path, remove

language = 'fr'
cachedAudio = {}

if __name__ == '__main__':
    audio_path = 'audioCache/'
    json_path = audio_path + 'cachedAudio.json'

else:
    audio_path = 'data/audioLib/audioCache/'
    json_path = audio_path + 'cachedAudio.json'


def readJSON(path):
    # read JSON from path, return dictionary output
    with open(path, 'r') as json_file:
        output_dict = load(json_file)
    return output_dict


def writeJSON(input_dict, path):
    # read dictionary, write to JSON at path, return nothing
    with open(path, 'w') as json_file:
        json_file.write(dumps(input_dict))


def preprocessText(text):
    # return 'Field Empty' if input is '', strip() text regardless
    if text == '':
        text = 'Field Empty'

    text = text.strip()
    return text


def generateKey(input_dict):
    # return 4 digit random key (string) not already in input_dict
    def generateKeyString():
        _key = str(randint(0, 9999999))

        while len(_key) < 8:
            _key = '0' + _key

        return _key

    key = generateKeyString()
    while key in input_dict:
        key = generateKeyString()

    return key


def KeyToFilePath(key):
    # return corresponding file path (string) of key (string)
    file_path = audio_path + key + '.mp3'
    return file_path


def entryInDict(input_entry, input_dict):
    # return array with boolean as to whether input_entry is in input_dict,
    # if yes, return key of input_entry, else return placeholder key of '0000'

    for key in input_dict:
        if input_entry == input_dict[key]:
            return [True, key]

    return [False, '0000']


def createAudioCache(input_text, input_dict, input_json):
    # generate unique key
    key = generateKey(input_dict)

    # create audio object
    audioObj = gTTS(text=input_text, lang=language)

    # save audio object to path
    audio_path = KeyToFilePath(key)
    audioObj.save(audio_path)

    # save to runtime dictionary, save to JSON
    input_dict[key] = input_text
    writeJSON(input_dict, input_json)


def sayText(input_text):
    global cachedAudio

    # check for empty input, strip()
    input_text = preprocessText(input_text)

    # load JSON
    cachedAudio = readJSON(json_path)

    # check in cachedAudio
    inAudioCache = entryInDict(input_text, cachedAudio)
    inAudioCacheBool = inAudioCache[0]

    if inAudioCacheBool:
        inAudioCacheKey = inAudioCache[1]
    else:
        createAudioCache(input_text, cachedAudio, json_path)
        inAudioCache = entryInDict(input_text, cachedAudio)
        inAudioCacheKey = inAudioCache[1]

    audio_path = KeyToFilePath(inAudioCacheKey)
    playsound(audio_path)


def clearAudioCache():
    global cachedAudio
    lsAudioCache = [_file for _file in listdir(audio_path) if _file.endswith('.mp3')]

    for _file in lsAudioCache:
        remove(path.join(audio_path, _file))

    cachedAudio = {}
    writeJSON(cachedAudio, json_path)


if __name__ == '__main__':
    from tkinter import Tk, Entry, Button
    from data.MyFunctions import makeGeometry

    test_root = Tk()
    test_root.geometry(makeGeometry(test_root, 200, 100))
    entry = Entry(test_root)
    entry.pack()


    def sayTextTest():
        sayText(entry.get())


    Button(test_root, text='SayEntryContent', command=sayTextTest).pack()
    Button(test_root, text='ClearAudioCache', command=clearAudioCache).pack()
    test_root.mainloop()



