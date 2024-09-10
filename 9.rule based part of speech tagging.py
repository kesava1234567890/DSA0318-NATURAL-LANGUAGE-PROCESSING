import re
rules = [
    (r'.*ing$', 'VBG'),   
    (r'.*ed$', 'VBD'),    
    (r'.*es$', 'VBZ'),    
    (r'.*ould$', 'MD'),   
    (r'.*\'s$', 'POS'),   
    (r'.*s$', 'NNS'),     
    (r'^-?[0-9]+$', 'CD'),
    (r'.*ly$', 'RB'),     
    (r'.*', 'NN')         
]

def tokenize(sentence):
    return sentence.split()
def pos_tag(tokens):
    tagged_sentence = []
    for token in tokens:
        tag = 'NN' 
        for pattern, rule_tag in rules:
            if re.match(pattern, token):
                tag = rule_tag
                break
        tagged_sentence.append((token, tag))
    return tagged_sentence

sentence = "The cats were quickly running towards the big house"
tokens = tokenize(sentence)
tagged_sentence = pos_tag(tokens)

print("Tagged Sentence:")
for token, tag in tagged_sentence:
    print(f"{token} -> {tag}")
