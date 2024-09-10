import nltk
from nltk import CFG
from nltk.tree import Tree
grammar = {
    'S': [['NP', 'VP']],   
    'NP': [['Det', 'N']],  
    'VP': [['V', 'NP']],   
    'Det': [['the'], ['a']], 
    'N': [['dog'], ['cat']], 
    'V': [['chases']]        
}
def tokenize(sentence):
    return sentence.split()
def parse(tokens, grammar, symbol):
    if not tokens:
        return False, []
    if symbol not in grammar:
        if tokens[0] == symbol:
            return True, tokens[1:] 
        else:
            return False, tokens
    for production in grammar[symbol]:
        remaining_tokens = tokens
        success = True
        for sym in production:
            success, remaining_tokens = parse(remaining_tokens, grammar, sym)
            if not success:
                break
        
       
        if success:
            return True, remaining_tokens

    return False, tokens
def parse_sentence(sentence, grammar, start_symbol='S'):
    tokens = tokenize(sentence)
    success, remaining_tokens = parse(tokens, grammar, start_symbol)
    
    if success and not remaining_tokens:
        print("Parsing successful!")
    else:
        print("Parsing failed.")
sentence = "the dog chases a cat"
parse_sentence(sentence, grammar)
cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chases'
""")
tokens = ['the', 'dog', 'chases', 'a', 'cat']

parser = nltk.ChartParser(cfg_grammar)

for tree in parser.parse(tokens):
    parse_tree = tree
    parse_tree.pretty_print()

    nltk.draw.tree.TreeView(parse_tree)._cframe.print_to_file("/mnt/data/parse_tree_output.png")
