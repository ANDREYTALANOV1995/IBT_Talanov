import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
#nltk.download()

res = requests.get('http://lib.ru')
res = res.content
res = BeautifulSoup(res)
res = nltk.Text(word_tokenize(res.text))
res = res.concordance('ФАНТАСТИКА')

print(res)

