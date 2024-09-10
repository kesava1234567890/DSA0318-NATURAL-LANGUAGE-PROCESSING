import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chases' | 'sees'
""")
sentence = ['the', 'dog', 'chases', 'a', 'cat']
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sentence):
    tree.pretty_print()
    
    
