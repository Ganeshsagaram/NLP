from nltk.corpus import movie_reviews
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
fields = movie_reviews.fileids()

sample = movie_reviews.raw("pos/cv944_13521.txt")

token = sent_tokenize(sample)
for words in token:
   if words not in stopwords.words('english'):
      print(words)
  
