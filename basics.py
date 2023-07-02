import nltk
from nltk.corpus import brown
from nltk.stem import PorterStemmer,WordNetLemmatizer
text='some words'
text.split(" ")
print(text)
print(nltk.sent_tokenize(text))
stemmer = PorterStemmer()
word = "running"
stemmed_word = stemmer.stem(word)
print("Stemmed word:", stemmed_word)
lema=WordNetLemmatizer()
lem=lema.lemmatize(word)
print(lem)