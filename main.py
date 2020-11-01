import requests
import json
import crawler.english_cambridge as cambridge
from Naked.toolshed.shell import muterun_js
import platform

if platform.system() == 'Windows':
    DOWNLOAD_DIR = 'C:/Users/Yu-Hsien/AppData/Roaming/Anki2/YuHsien/collection.media/'
    JP_CRAWLER_PATH = 'C:/Users/Yu-Hsien/Desktop/crawler/littleD.js'
elif platform.system() == 'Darwin':
    DOWNLOAD_DIR = '/Users/pacsoft/Library/Application Support/Anki2/YuHsien/collection.media/'
    JP_CRAWLER_PATH = '/Users/pacsoft/Desktop/littleDCrawler/littleD.js'

EN_INPUT_FILE = 'input_EN.txt'
JP_INPUT_FILE = 'littleDJSON.json'
JP_SENTENCE_INPUT_FILE = 'input_JP_sentence.json'

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

# Run JP Crawler
js_response = muterun_js(JP_CRAWLER_PATH, 'python')
if js_response.exitcode == 0:
    print(js_response.stdout.decode("utf-8"))
else:
    print(js_response.stderr)
add_JP_cards(JP_INPUT_FILE, jp_note_template)

# Run EN Crawler
with open(EN_INPUT_FILE , encoding='utf-8') as word_list:
    for word in word_list:
        word = word.splitlines()[0]
        en_note_template['fields'] = cambridge.LookUp(word, DOWNLOAD_DIR)
        response = api('addNote', **{ "note": en_note_template })
        print('API Response:', response.json())

# Run JP Sentence Input
add_JP_cards(JP_SENTENCE_INPUT_FILE, jp_sentence_note_template)