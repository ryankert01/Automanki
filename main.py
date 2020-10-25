import requests
import json
import crawler.english_cambridge as cambridge

DOWNLOAD_DIR = 'C:/Users/Yu-Hsien/AppData/Roaming/Anki2/YuHsien/collection.media/'
INPUT_FILE = 'input.txt'
START = 'start'
END_OF_DICT = '----'

en_note_template = {
    "deckName": "英文",
    "modelName": "基本型(含反向的卡片)",
    "fields": {},
}

jp_note_template = {
    "deckName": "日文",
    "modelName": "Japanese (recognition&recall)",
    "fields": {},
}

def api (action, **params):
    return requests.post('http://localhost:8765', json.dumps({
        "action": action,
        "version": 6,
        "params": params,
    }))

payload = {
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
            "deckName": "英文",
            "modelName": "基本型(含反向的卡片)",
            "fields": {
                "正面": "front content",
                "背面": "back content"
            },
            # "options": {
            #     "allowDuplicate": False,
            #     "duplicateScope": "deck"
            # },
            # "tags": [
            #     "yomichan"
            # ],
            # "audio": [{
            #     "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
            #     "filename": "yomichan_ねこ_猫.mp3",
            #     "skipHash": "7e2c2f954ef6051373ba916f000168dc",
            #     "fields": [
            #         "正面"
            #     ]
            # }]
        }
    }
}
TARGET = ['[英文]', '[日文單字]', '[日文動詞]']

# # Get deck names
# response = api('deckNames')
# deckNames = response.json()['result']
# print(deckNames)

# # Get model names
# response = api('modelNames')
# modelNames = response.json()['result']
# print(modelNames)

stat = None
target = None
with open(INPUT_FILE , encoding='utf-8') as word_list:
    for word in word_list:
        word = word.splitlines()[0]
        if stat == START:
            if word != END_OF_DICT:
                if target == '[英文]':
                    en_note_template['fields'] = cambridge.LookUp(word, DOWNLOAD_DIR)
                    response = api('addNote', **{ "note": en_note_template })
                    print(response.json())
                else:
                    print('JP')
            else:
                stat = None
        elif word in TARGET:
            target = word
            stat = START