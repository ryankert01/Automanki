# Automanki

This project provides a convenient way for Anki user to add anki card. We used [anki-connect](https://github.com/FooSoft/anki-connect) and the web crawler of [Ankieasy](https://github.com/ex860/Ankieasy) and [littleDCrawler](https://github.com/ex860/littleDCrawler) to create a automated program.

> This program requires [anki-connect Anki plugin](https://ankiweb.net/shared/info/2055492159)

- Uasge
  - Open Anki
  - Enter your anki collection.media absolute path in variable DOWNLOAD_DIR in `main.py` (the path of littleD.js in JP_CRAWLER_PATH if needed)
  - Enter one word per line in the input text file and save it. (Apparently, `input_EN.txt` is for English and `input_JP.txt` is for Japanese)
  - execute `python main.py` or `python3 main.py` due to your environment
