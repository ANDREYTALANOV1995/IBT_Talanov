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

res234 = [s for s in result if "Повесть" in s]

res234 = re.findall(r'\/.*shtml', res234[0])

s_fan2 = requests.get(url + res234[0])

result = re.findall(r'(DT.*?)(\/\S*shtml)|(;\s\s.*?<)', s_fan2.text)

name = []
link = []

for i in result:
    if i[2] != '':
        name.append(i[2][2:-2])
    if i[1] != '':
        link.append(url + i[1])



file = open('book/text6.txt')
book1 = file.read()  # Хоббит
file.close()
file = open('book/text1.txt')
book2 = file.read()  # Ведьмак
file.close()
file = open('book/text2.txt')
book3 = file.read()  # Игра престолов
file.close()
file = open('book/book2.txt')
book5 = file.read()
file.close()
file = open('book/book3.txt')
book6 = file.read()
file.close()
file = open('stop_words.txt')
stop_words = file.read()
file.close()
sw = nltk.word_tokenize(stop_words)
stop_words = stopwords.words('russian')
stop_words.extend(sw)

#функция для получение 150 самых распространеных слов

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

#------------------------получаем эталон из популярных книг

data1 = np.array(tokenize_me(book1))
data2 = np.array(tokenize_me(book2))
data3 = np.array(tokenize_me(book3))
data5 = np.array(tokenize_me(book5))
data6 = np.array(tokenize_me(book6))



res = []
res2 = []


for data in np.intersect1d(data1, data2):
    res.append(data)
for data in np.intersect1d(res, data3):
    res.append(data)
for data in np.intersect1d(data6, data5):
    res2.append(data)


res = set(res)
res2 = set(res2)

#---------------------------------------------------------

# функция для проверки входящего текста по эталону фентези

def isFan(token):
    token = tokenize_me(token)
    mat = []
    for m in res:
        if m in token:
            mat.append(1)
        else:
            mat.append(0)

    return sum(mat)/len(res)

# функция для проверки входящего текста по эталону киберпанка

def isCyb(token):
    token = tokenize_me(token)
    mat = []
    for n in res2:
        if n in token:
            mat.append(1)
        else:
            mat.append(0)

    return sum(mat)/len(res2)

print('хоббит-', isFan(book1)*100 ,'%')

for i in range(10):
    f_b = requests.get(link[i])
    op = bs4.BeautifulSoup(f_b.text, "html.parser").getText()

    print(link[i])
    print('Экспертное мнение|', name[i])

    if isFan(op):
        print("программа считает, что это Фэнтези|", round(isFan(op)*100), '%')
    if isCyb(op):
        print("программа считает, что это киберпанк|", round(isCyb(op)*100), '%')


    print("________________________")

print("end")
