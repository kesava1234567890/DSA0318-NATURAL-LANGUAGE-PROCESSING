import spacy
import neuralcoref
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

def resolve_coreferences(text):
    doc = nlp(text)
    if doc._.has_coref:
        return doc._.coref_resolved
    else:
        return "No coreference found."
text = "John went to the park. He played soccer there with his friends."

resolved_text = resolve_coreferences(text)
print("Original Text:\n", text)
print("\nResolved Text:\n", resolved_text)
