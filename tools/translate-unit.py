#Unit tests for translate.py

from translate import *

text = '纽约时报中文网国际纵览'
lang = gtDetectLang(text)
print ('The detected language is ' + lang)

result = gtAutoTranslate(text)
print(text + ' using autodetection of language is ' + result)

result = gtTranslate(text, lang)
print(text + ' using explicit language def is ' + result)
