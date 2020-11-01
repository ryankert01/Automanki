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
JP_OUTPUT_FILE = 'littleDJSON.json'

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

# Run JP Crawler
response = muterun_js(JP_CRAWLER_PATH, 'python')
if response.exitcode == 0:
    print(response.stdout.decode("utf-8"))
else:
    print(response.stderr)
with open(JP_OUTPUT_FILE, encoding='utf-8') as output:
    notes = map(lambda x: { **jp_note_template, "fields": x }, json.load(output))
    response = api('addNotes', **{ "notes": list(notes) })
    print('API Response:', response.json())

# Run EN Crawler
with open(EN_INPUT_FILE , encoding='utf-8') as word_list:
    for word in word_list:
        word = word.splitlines()[0]
        en_note_template['fields'] = cambridge.LookUp(word, DOWNLOAD_DIR)
        response = api('addNote', **{ "note": en_note_template })
        print('API Response:', response.json())