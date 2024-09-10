import spacy
nlp = spacy.load("en_core_web_sm")
def perform_ner(text):
    doc = nlp(text)
    print("Named Entities, Phrases, and Concepts:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")
if __name__ == "__main__":
    text = ("Apple is looking at buying U.K. startup for $1 billion. "
            "Barack Obama was born in Hawaii.")
    perform_ner(text)
