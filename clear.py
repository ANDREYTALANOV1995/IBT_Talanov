
#nltk.download('punkt')
#nltk.download('stopwords')

import string
from nltk.corpus import stopwords
import numpy as np
import nltk
import requests
import bs4

s_fan1 = requests.get('http://lib.ru/SOCFANT/HOBANE/01-68.txt')
s_fan2 = requests.get('http://lib.ru/ADAMS/hitch_3_sp.txt')
s_fan3 = requests.get('http://lib.ru/INOFANT/BINEM/03-63.txt')
tales1 = requests.get('http://lib.ru/TALES/alenkij.txt')
tales2 = requests.get('http://lib.ru/DETEKTIWY/AJRISH/windows.txt')

f_1 = bs4.BeautifulSoup(s_fan1.text, "html.parser")
f_2 = bs4.BeautifulSoup(s_fan2.text, "html.parser")
f_3 = bs4.BeautifulSoup(s_fan2.text, "html.parser")
f_4 = bs4.BeautifulSoup(tales1.text, "html.parser")
f_5 = bs4.BeautifulSoup(tales2.text, "html.parser")


file = open('book/text6.txt')
book1 = file.read()  # Хоббит
file = open('book/text1.txt')
book2 = file.read()  # Ведьмак
file = open('book/text2.txt')
book3 = file.read()  # Игра престолов
file = open('book/text3.txt')
book4 = file.read()  # Хроники нарнии
file = open('book/text4.txt')
book5 = file.read()  # Ромео и Джульетта
file = open('book/text5.txt')
book6 = file.read()  # 451 градус по Фаренгейту


def tokenize_me(file_text):
    stop = open('stop_words.txt')
    sw = stop.read()
    sw = nltk.word_tokenize(sw)

    res = []

    tokens = file_text.lower()

    tokens = nltk.word_tokenize(tokens)

    tokens = [i for i in tokens if (i not in string.punctuation)]

    stop_words = stopwords.words('russian')
    stop_words.extend(sw)

    tokens = [i for i in tokens if (i not in stop_words)]

    tokens = [i.replace("«", "").replace("»", "") for i in tokens]

    tokens = nltk.FreqDist(tok for tok in tokens)

    tokens = tokens.most_common(150)

    for tok in tokens:
        res.append(tok[0])

    return res


def isFan(token):
    token = tokenize_me(token)

    data1 = np.array(tokenize_me(book1))
    data2 = np.array(tokenize_me(book2))
    data3 = np.array(tokenize_me(book3))
    res = []
    mat = []

    for data in np.intersect1d(data1, data2):
        res.append(data)
    for data in np.intersect1d(res, data3):
        res.append(data)

    res = set(res)

    for re in res:
        if re in token:
            mat.append(1)
        else:
            mat.append(0)

    if sum(mat) > 20:
        res = "true"
    else:
        res = "false"

    return res


print(isFan(book4))

print("________________________")

print(isFan(book6))

print("________________________")

print(isFan(book5))

print("_________с сайта lib.ru_______________")

print(isFan(f_1.getText()))

print("________________________")

print(isFan(f_2.getText()))

print("________________________")

print(isFan(f_3.getText()))

print("________________________")

print(isFan(f_4.getText()))

print("________________________")

print(isFan(f_5.getText()))
