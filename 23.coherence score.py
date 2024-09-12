from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calculate_coherence(text):
    sentences = text.split(".")
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    if len(sentences) < 2:
    embeddings = model.encode(sentences)
    similarities = []
    for i in range(len(embeddings) - 1):
        sim = cosine_similarity([embeddings[i]], [embeddings[i + 1]])[0][0]
        similarities.append(sim)
    average_coherence = np.mean(similarities)
    return average_coherence
text = """
Artificial intelligence is transforming the world. It is being applied in various industries. 
From healthcare to finance, AI is making processes more efficient. 
The technology still has challenges. However, continuous advancements are being made.
"""

coherence_score = calculate_coherence(text)
print(f"Coherence score: {coherence_score:.4f}")
