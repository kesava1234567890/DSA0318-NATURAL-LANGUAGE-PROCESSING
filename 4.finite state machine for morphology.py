def fsm_plural(noun):
    if noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    
    else:
        return noun + 's'
nouns = ['cat', 'dog', 'bus', 'church', 'fox', 'baby', 'lady', 'hero']

for noun in nouns:
    plural_form = fsm_plural(noun)
    print(f"Singular: {noun}, Plural: {plural_form}")
