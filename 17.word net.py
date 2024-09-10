import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
def explore_word(word):
    synsets = wordnet.synsets(word)
    
    if not synsets:
        print(f"No synsets found for the word '{word}'.")
        return
    
    print(f"Synsets for the word '{word}':\n")
    
    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}\n")
        lemmas = synset.lemmas()
        synonyms = [lemma.name() for lemma in lemmas]
        print(f"Synonyms: {', '.join(set(synonyms))}\n")
        hypernyms = synset.hypernyms()
        hypernym_names = [hypernym.name() for hypernym in hypernyms]
        print(f"Hypernyms: {', '.join(hypernym_names)}\n")

if __name__ == "__main__":
    word = "bank"  
    explore_word(word)
