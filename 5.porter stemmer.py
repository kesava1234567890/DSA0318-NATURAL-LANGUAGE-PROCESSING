import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
stemmer = PorterStemmer()
words = ["running", "jumps", "easily", "fairly", "happiness", "cats", "studying", "flying"]
stemmed_words = [stemmer.stem(word) for word in words]
for word, stemmed in zip(words, stemmed_words):
    print(f"Original Word: {word}, Stemmed Word: {stemmed}")
