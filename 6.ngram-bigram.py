import random
import nltk
nltk.download('punkt_tab')
from nltk import bigrams, word_tokenize
from collections import defaultdict
text = """
The quick brown fox jumps over the lazy dog. The dog barked at the fox. The fox ran away quickly.
"""
nltk.download('punkt')
tokens = word_tokenize(text.lower())
bigram_model = defaultdict(list)
for word1, word2 in bigrams(tokens):
    bigram_model[word1].append(word2)
def generate_bigram_text(start_word, num_words):
    current_word = start_word
    output = [current_word]
    
    for _ in range(num_words - 1):  
        next_words = bigram_model.get(current_word, None)
        if not next_words: 
            break
        next_word = random.choice(next_words)
        output.append(next_word)
        current_word = next_word
    
    return ' '.join(output)
start_word = "the"
generated_text = generate_bigram_text(start_word, 10)
print(f"Generated Text: {generated_text}")
