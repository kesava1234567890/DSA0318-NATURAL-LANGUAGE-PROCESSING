import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
def pos_tagging(text):    
    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    return tagged_words
text = "This is a sample sentence for part-of-speech tagging using NLTK."
tagged_text = pos_tagging(text)
print(tagged_text)

