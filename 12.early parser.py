import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chases' | 'sees'
""")
sentence = ['the', 'dog', 'chases', 'a', 'cat']
earley_parser = EarleyChartParser(grammar)
parses = list(earley_parser.parse(sentence))
for tree in parses:
    tree.pretty_print()
for tree in parses:
    nltk.draw.tree.TreeView(tree)._cframe.print_to_file("/mnt/data/earley_parse_tree_output.png")
