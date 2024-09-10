from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "The cat in the hat.",
    "The quick brown fox jumped over the lazy dog.",
    "The cat is sleeping on the mat.",
    "The dog is in the park."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
query = "cat on the mat"
query_tfidf = vectorizer.transform([query])
cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix)
print("Ranking of documents based on query similarity:")
for index, score in enumerate(cosine_similarities[0]):
    print(f"Document {index}: {score:.4f}")
most_similar_document_index = cosine_similarities[0].argmax()
print("\nMost similar document to the query:")
print(documents[most_similar_document_index])
