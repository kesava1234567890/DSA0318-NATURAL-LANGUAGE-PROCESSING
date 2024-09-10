import nltk
from nltk.corpus import brown
from collections import defaultdict
import random

# Download necessary resources
nltk.download('brown')
nltk.download('universal_tagset')

# Step 1: Load a tagged corpus (Brown corpus with universal tagset for simplicity)
tagged_sentences = brown.tagged_sents(tagset='universal')

# Step 2: Calculate transition probabilities (bigram probabilities)
# Transition probability: P(tag|previous_tag)
transition_probs = defaultdict(lambda: defaultdict(lambda: 0))

# Count occurrences of tag pairs
for sentence in tagged_sentences:
    previous_tag = '<START>'
    for word, tag in sentence:
        transition_probs[previous_tag][tag] += 1
        previous_tag = tag
    transition_probs[previous_tag]['<END>'] += 1

# Normalize to get probabilities
for prev_tag in transition_probs:
    total = sum(transition_probs[prev_tag].values())
    for tag in transition_probs[prev_tag]:
        transition_probs[prev_tag][tag] /= total

# Step 3: Calculate emission probabilities (likelihood of word given tag)
# Emission probability: P(word|tag)
emission_probs = defaultdict(lambda: defaultdict(lambda: 0))

# Count occurrences of word given tag
for sentence in tagged_sentences:
    for word, tag in sentence:
        emission_probs[tag][word.lower()] += 1

# Normalize to get probabilities
for tag in emission_probs:
    total = sum(emission_probs[tag].values())
    for word in emission_probs[tag]:
        emission_probs[tag][word] /= total

# Step 4: POS tagging using a basic probabilistic model
def stochastic_pos_tag(sentence):
    # Start with the initial tag <START>
    prev_tag = '<START>'
    tagged_sentence = []

    for word in sentence:
        # Find the most probable tag for the current word
        possible_tags = emission_probs.keys()
        best_tag = max(possible_tags, key=lambda tag: transition_probs[prev_tag].get(tag, 0) * emission_probs[tag].get(word.lower(), 0.0001))
        tagged_sentence.append((word, best_tag))
        prev_tag = best_tag

    return tagged_sentence

# Example sentence to tag
sentence = "The quick brown fox jumps over the lazy dog".split()

# Tag the sentence
tagged_sentence = stochastic_pos_tag(sentence)

# Output the tagged sentence
for word, tag in tagged_sentence:
    print(f"{word}: {tag}")
