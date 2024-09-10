# Importing necessary libraries
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download necessary resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Example text
text = "The striped bats are hanging on their feet for best"

# Tokenize the text into words
tokens = word_tokenize(text)

# Stemming using PorterStemmer
stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in tokens]

# Lemmatization using WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token, pos='v') for token in tokens]  # 'v' is for verb context

# Display results
print(f"Original Words: {tokens}")
print(f"Stemmed Words: {stems}")
print(f"Lemmatized Words: {lemmas}")
