import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')

def lesk_algorithm(context_sentence, target_word):
    context_words = set(context_sentence.lower().split())
    synsets = wordnet.synsets(target_word)
    best_sense = None
    max_overlap = 0
    
    for synset in synsets:
        
        gloss = synset.definition().lower() + ' ' + ' '.join(synset.examples()).lower()
        gloss_words = set(gloss.split())
        
        
        overlap = len(context_words.intersection(gloss_words))
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset
    
    return best_sense

if __name__ == "__main__":
    context_sentence = "He went to the bank to deposit money."
    target_word = "bank"
    
    sense = lesk_algorithm(context_sentence, target_word)
    
    if sense:
        print(f"The most likely sense for '{target_word}' is:")
        print(f"Synset: {sense.name()}")
        print(f"Definition: {sense.definition()}")
        print(f"Examples: {sense.examples()}")
    else:
        print(f"No sense found for the word '{target_word}'.")
