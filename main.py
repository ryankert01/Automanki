import requests
import json
import crawler.english_cambridge as cambridge

import platform
import re

if platform.system() == 'Windows':
    DOWNLOAD_DIR = 'C:/Users/tang/AppData/Roaming/Anki2/使用者 1/collection.media/'
elif platform.system() == 'Darwin':
    DOWNLOAD_DIR = '/Users/pacsoft/Library/Application Support/Anki2/YuHsien/collection.media/'
elif platform.system() == 'Linux':
    print("Linux!")

EN_INPUT_FILE = 'input_EN.txt'
JP_INPUT_FILE = 'littleDJSON.json'
JP_SENTENCE_INPUT_FILE = 'input_JP_sentence.json'

en_note_template = {
    "deckName": "英文::論文",
    "modelName": "細分版",
    "fields": {},
}

jp_note_template = {
    "deckName": "日文",
    "modelName": "Japanese (recognition&recall)",
    "fields": {},
}

jp_sentence_note_template = {
    "deckName": "日文句子",
    "modelName": "Japanese (recognition&recall)",
    "fields": {},
}

def api(action, **params):
    return requests.post('http://localhost:8765', json.dumps({
        "action": action,
        "version": 6,
        "params": params,
    }))

def add_JP_cards(input_file, note_template):
    with open(input_file, encoding='utf-8') as json_file:
        inputs = json.load(json_file)
        if len(inputs) > 0:
            notes = map(lambda x: { **note_template, "fields": x }, inputs)
            response = api('addNotes', **{ "notes": list(notes) })
            print('API Response:', response.json())



# Run EN Crawler
with open(EN_INPUT_FILE , encoding='utf-8') as word_list:
    word_list = filter(lambda x:  not re.match(r'^\s*$', x), word_list) #
    for word in word_list:
        word = word.splitlines()[0]
        en_note_template['fields'] = cambridge.LookUp(word, DOWNLOAD_DIR)
        response = api('addNote', **{ "note": en_note_template })
        print('API Response:', response.json())

# Run JP Sentence Input
add_JP_cards(JP_SENTENCE_INPUT_FILE, jp_sentence_note_template)