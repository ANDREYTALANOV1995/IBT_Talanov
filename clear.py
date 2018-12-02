import nltk
import string
from nltk.corpus import stopwords

file = open('text.txt')
text = file.read()

file1 = open('text1.txt')
text1 = file1.read()

def tokenize_me(file_text):

	tokens = file_text.lower()

	tokens = nltk.word_tokenize(tokens)

	tokens = [i for i in tokens if (i not in string.punctuation)]

	stop_words = stopwords.words('russian')
	stop_words.extend(['что', 'что-то', 'это', 'так', 'вот', 'быть', 'как', 'из-за', 'в', '–', '—', 'к', 'на', 'вовсе', 'где', 'и', 'а', 'те', 'нам'])

	tokens = [i for i in tokens if (i not in stop_words)]

	tokens = [i.replace("«", "").replace("»", "") for i in tokens]

	tokens = nltk.FreqDist(tok for tok in tokens)

	return tokens.most_common(100)


print(tokenize_me(text))



