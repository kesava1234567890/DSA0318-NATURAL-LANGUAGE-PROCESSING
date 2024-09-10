import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | Det N PP
  PP -> P NP
  VP -> V NP | V NP PP
  Det -> 'a' | 'an' | 'the'
  N -> 'dog' | 'cat' | 'park' | 'telescope'
  V -> 'saw' | 'ate' | 'walked'
  P -> 'in' | 'on' | 'by' | 'with'
""")
def check_sentence(sentence):
    tokens = sentence.lower().split()
    
    parser = EarleyChartParser(grammar)
    parses = list(parser.parse(tokens))
    
    if parses:
        print("The sentence is valid according to the grammar.")
        return True
    else:
        print("The sentence is not valid according to the grammar.")
        return False
if __name__ == "__main__":
    sentence = "the dog saw a cat in the park"
    check_sentence(sentence)
