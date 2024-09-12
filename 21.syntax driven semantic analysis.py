import spacy
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

nlp = spacy.load('en_core_web_sm')

def get_noun_phrases_and_meanings(sentence):
    doc = nlp(sentence)
    
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    noun_phrases_meanings = {}


    for phrase in noun_phrases:
        words = word_tokenize(phrase)
        meanings = []
        for word in words:
            synsets = wn.synsets(word)
            if synsets:
                meanings.append(synsets[0].definition())
        noun_phrases_meanings[phrase] = meanings

    return noun_phrases, noun_phrases_meanings

sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases, meanings = get_noun_phrases_and_meanings(sentence)

print("Noun Phrases:", noun_phrases)
print("Meanings:")
for phrase, meaning in meanings.items():
    print(f"{phrase}: {', '.join(meaning)}")
