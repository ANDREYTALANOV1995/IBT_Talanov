import string
from nltk.corpus import stopwords
import numpy as np
import nltk
import requests
import bs4

# for book in books:
# parsers.append(BS(get().content))
import re

# поиск по сайту
url = 'http://fan.lib.ru/'

s_fan1 = requests.get(url)

result = re.findall(r'<a href=.*?a>', s_fan1.text)

res234 = [s for s in result if "Фэнтези" in s]

res234 = re.findall(r'\/.*shtml', res234[0])

s_fan2 = requests.get(url + res234[0])

result2 = re.findall(r'\/\S*shtml', s_fan2.text)

file = open('book/text6.txt')
book1 = file.read()  # Хоббит
file.close()
file = open('book/text1.txt')
book2 = file.read()  # Ведьмак
file.close()
file = open('book/text2.txt')
book3 = file.read()  # Игра престолов
file.close()
file = open('stop_words.txt')
stop_words = file.read()
file.close()
sw = nltk.word_tokenize(stop_words)
stop_words = stopwords.words('russian')
stop_words.extend(sw)

def tokenize_me(file_text):
    res = []

    tokens = file_text.lower()

    tokens = nltk.word_tokenize(tokens)

    tokens = [i for i in tokens if (i not in string.punctuation)]

    tokens = [i for i in tokens if (i not in stop_words)]

    tokens = [i.replace("«", "").replace("»", "") for i in tokens]

    tokens = nltk.FreqDist(tok for tok in tokens)

    tokens = tokens.most_common(150)

    for tok in tokens:
        res.append(tok[0])

    return res


data1 = np.array(tokenize_me(book1))
data2 = np.array(tokenize_me(book2))
data3 = np.array(tokenize_me(book3))
res = []


for data in np.intersect1d(data1, data2):
    res.append(data)
for data in np.intersect1d(res, data3):
    res.append(data)

res = set(res)


def isFan(token):
    token = tokenize_me(token)
    mat = []
    for re in res:
        if re in token:
            mat.append(1)
        else:
            mat.append(0)

    return sum(mat) > 18



for re in result2:
    link_f = url + re
    f_b = requests.get(link_f)
    op = bs4.BeautifulSoup(f_b.text, "html.parser").getText()
    if isFan(op):
        print('Фэнтези=', link_f)
        print("________________________")

print("end")