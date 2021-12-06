# AutoAnki

## Introduction
這個程式主要是輔助Anki這套自卡系統使用，這邊提自動製作字卡的服務。
基於使用者指定的單字，從[劍橋字典](https://dictionary.cambridge.org/zht/)抓取 中英、英英、發音、例句 製作成單字卡。


## Dependencies
|Name|
|----|
|lxml|
|requests|
|BeautifulSoup4|

## Usage

### 1. 打開 Anki

### 2. 在 `input_EN.txt` 新增單字，格式如下:
```
apple
orange
```

### 3. 修改 `main.py` 中的變量 DOWNLOAD_DIR : 請輸入本機anki應用程式中 collection.media 的絕對路徑
```
 DOWNLOAD_DIR = 'C:/Users/tang/AppData/Roaming/Anki2/使用者 1/collection.media/'
```

### 3. 執行 `main.py`
```
$ python main.py
```
