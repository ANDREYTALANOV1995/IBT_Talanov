import requests

import nltk
from nltk.tokenize import word_tokenize

import bs4


res = requests.get('http://lib.ru')
res = res.content
res = bs4.BeautifulSoup(res, features="html.parser")
res = nltk.Text(word_tokenize(res.text))
res = res.concordance('ФАНТАСТИКА')

print('результат', res)

