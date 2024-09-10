import re
transformation_rules = [
   
    (r'NN', 'VB', lambda sentence, i: sentence[i-1][1] == 'TO'),

    
    (r'NN', 'JJ', lambda sentence, i: sentence[i-1][1] == 'DT'),
]
def tokenize(sentence):
    return sentence.split()
def initial_tagger(tokens):
    return [(token, 'NN') for token in tokens]
def apply_transformation_rules(tagged_sentence, rules):
    for i in range(1, len(tagged_sentence)):
        token, tag = tagged_sentence[i]
        for old_tag, new_tag, condition in rules:
            if tag == old_tag and condition(tagged_sentence, i):
                tagged_sentence[i] = (token, new_tag)
                break
    return tagged_sentence
sentence = "I want to swim in the clear lake"
tokens = tokenize(sentence)
tagged_sentence = initial_tagger(tokens)
print("Initially Tagged Sentence:", tagged_sentence)
transformed_sentence = apply_transformation_rules(tagged_sentence, transformation_rules)

print("Transformed Tagged Sentence:")
for token, tag in transformed_sentence:
    print(f"{token} -> {tag}")
