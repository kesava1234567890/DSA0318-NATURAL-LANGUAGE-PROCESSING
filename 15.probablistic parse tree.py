import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det N [0.6] | Det N PP [0.4]
  PP -> P NP [1.0]
  VP -> V NP [0.7] | V NP PP [0.3]
  Det -> 'a' [0.2] | 'an' [0.3] | 'the' [0.5]
  N -> 'dog' [0.4] | 'cat' [0.4] | 'park' [0.1] | 'telescope' [0.1]
  V -> 'saw' [0.3] | 'ate' [0.4] | 'walked' [0.3]
  P -> 'in' [0.4] | 'on' [0.3] | 'by' [0.2] | 'with' [0.1]
""")

def parse_sentence(sentence):
    tokens = sentence.lower().split()
    
    parser = ViterbiParser(grammar)
    
    parses = list(parser.parse(tokens))
    
    if not parses:
        print("No valid parse found.")
        return
    
    best_parse = parses[0]  
    print("The most probable parse tree:")
    best_parse.pretty_print()
if __name__ == "__main__":
    sentence = "the dog saw a cat in the park"
    parse_sentence(sentence)
