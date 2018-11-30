import nltk
import string
from nltk.corpus import stopwords

def tokenize_me(file_text):

	tokens = nltk.word_tokenize(file_text)

	tokens = [i for i in tokens if (i not in string.punctuation)]

	stop_words = stopwords.words('russian')
	stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'В', '—', 'К', 'на', 'вовсе', 'где', 'И', 'А'])
	tokens = [i for i in tokens if (i not in stop_words)]

	# cleaning words
	tokens = [i.replace("«", "").replace("»", "") for i in tokens]
	return tokens


